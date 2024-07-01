import requests
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from load_env import cemaden_api_token, user_cemaden, password_cemaden
from config_db import consultar_ultimo_registro_estacao
from config_db_Apac import consultar_ultimo_registro_tendencia

def grafico_heatmap():
    st.markdown("## Acumulado + Tendência APAC por Risco")
    
    token_url = cemaden_api_token
    login = {'email': user_cemaden, 'password': password_cemaden}
    response = requests.post(token_url, json=login)

    if response.status_code == 200:
        content = response.json()
        token = content['token']

        dados = consultar_ultimo_registro_estacao('260790106A')
        
        (id, val_120h, val_12h, val_1h, val_24h, val_3h, val_48h, val_6h, val_72h, val_96h, estacao, codigo, data_hora, outro_valor, local) = dados
        
        # Calcular a data de 6 dias atrás no formato desejado
        data5dAtras = (datetime.now() - timedelta(days=5)).strftime('%Y%m%d%H%M')
        data10dAtras = (datetime.now() - timedelta(days=10)).strftime('%Y%m%d%H%M')

        sws_url = 'http://sws.cemaden.gov.br/PED/rest/pcds-acum/acumulados-historicos'
        params = dict(codibge=2607901, codestacao='260790106A', data=data5dAtras)
        s = requests.get(sws_url, params=params, headers={'token': token})

        dados_json = s.json()

        if dados_json:
            dados = dados_json[0]
            acc24hr_6d = dados['acc24hr']
            acc120hr_6d = dados['acc120hr']
        else:
            print("A lista está vazia.")
            acc120hr_6d = 0 

        
        sws_url = 'http://sws.cemaden.gov.br/PED/rest/pcds-acum/acumulados-historicos'
        params = dict(codibge=2607901, codestacao='260790106A', data=data10dAtras)
        f = requests.get(sws_url, params=params, headers={'token': token})

        dados_json_10d = f.json()
        if dados_json_10d:
            dados_10d = dados_json_10d[0]
            acc120hr_10d = dados_10d['acc120hr']
        else:
            print("A lista está vazia.")
            acc120hr_10d = 0 
            
        dados_tendencia = consultar_ultimo_registro_tendencia()
        apac_1dia = dados_tendencia[-1][-1]
        apac_2dia = dados_tendencia[-2][-1]
        
        tendencia_3d_apac1 = round(float(val_72h) + float(apac_1dia), 2)
        tendencia_3d_apac2 = round(float(val_72h) + float(apac_2dia), 2)
        tendencia_6d_apac1 = round(float(val_120h) + float(acc24hr_6d) + float(apac_1dia), 2)
        tendencia_6d_apac2 = round(float(val_120h) + float(acc24hr_6d) + float(apac_2dia), 2)
        tendencia_10d_apac1 = round(float(val_120h) + float(acc120hr_6d) + float(acc120hr_10d) + float(apac_1dia), 2)
        tendencia_10d_apac2 = round(float(val_120h) + float(acc120hr_6d) + float(acc120hr_10d) + float(apac_2dia), 2)
        acumulado_6d = round(float(val_120h) + float(acc24hr_6d), 2)
        acumulado_10d = round(float(val_120h) + float(acc120hr_6d) + float(acc120hr_10d), 2)
        
        data = {
            "Acumulado": [val_72h, acumulado_6d, acumulado_10d],
            "+1 dia Apac": [tendencia_3d_apac1, tendencia_6d_apac1, tendencia_10d_apac1],
            "+2 dias Apac": [tendencia_3d_apac2, tendencia_6d_apac2, tendencia_10d_apac2],
        }

        # Atualizar o índice do DataFrame
        df = pd.DataFrame(data, index=["3 dias Impacto Extremo", "6 dias Impacto Alto", "15 dias Impacto Moderado"])

        def get_color(value, period):
            if period == "3 dias Impacto Extremo":
                if value < 70:
                    return '#00FF00'  # Verde
                elif 70 <= value < 100:
                    return '#FFFF00'  # Amarelo
                else:
                    return '#FF0000'  # Vermelho
            elif period == "6 dias Impacto Alto":
                if value < 105:
                    return '#00FF00'  # Verde
                elif 105 <= value < 150:
                    return '#FFFF00'  # Amarelo
                else:
                    return '#FF0000'  # Vermelho
            elif period == "15 dias Impacto Moderado":
                if value < 140:
                    return '#00FF00'  # Verde
                elif 140 <= value < 200:
                    return '#FFFF00'  # Amarelo
                else:
                    return '#FF0000'  # Vermelho

        colors = df.applymap(lambda x: get_color(x, df.index[df.applymap(lambda y: y == x).any()][0]))

        fig, ax = plt.subplots(figsize=(10, 4))

        for y in range(df.shape[0]):
            for x in range(df.shape[1]):
                ax.text(x + 0.5, y + 0.5, f'{df.iloc[y, x]:.2f}', 
                        ha='center', va='center', color='black', fontsize=12, weight='bold')
                ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=True, color=colors.iloc[y, x], lw=0))

        ax.set_xticks([0.5, 1.5, 2.5])
        ax.set_xticklabels(df.columns)
        ax.set_yticks([0.5, 1.5, 2.5])
        ax.set_yticklabels(df.index)
        ax.set_xlim(0, df.shape[1])
        ax.set_ylim(0, df.shape[0])
        ax.invert_yaxis()

        # Adicionar textos adicionais para a escala de risco
        plt.text(3.5, 2.5, "Baixo", ha="center", va="center", color="green", size="x-large")
        plt.text(3.5, 1.5, "Moderado", ha="center", va="center", color="orange", size="x-large")
        plt.text(3.5, 0.5, "Alerta", ha="center", va="center", color="red", size="x-large")

        st.pyplot(fig)
