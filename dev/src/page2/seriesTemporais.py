import pandas as pd
import streamlit as st
from config_db import consultar_estacoes_disponiveis_e_ultimos_registros
from datetime import timedelta
import plotly.express as px
from src.utils.auto_refresh import atualizarPage

def series_temporais(widthImage):
    try:
        atualizarPage()
        # Consultar os dados das estações e seus últimos registros
        dados = consultar_estacoes_disponiveis_e_ultimos_registros()
        
        # Filtrar dados válidos e organizar em um DataFrame
        dados_validos = [dado for dado in dados if dado is not None]
        colunas = [
            'id', 'acc120hr', 'acc12hr', 'acc1hr', 'acc24hr', 'acc3hr', 'acc48hr',
            'acc6hr', 'acc72hr', 'acc96hr', 'codestacao', 'codibge', 'datahora', 'id_estacao', 'nome_estacao', 'regiao'
        ]
        df = pd.DataFrame(dados_validos, columns=colunas)
        
        # Transformar a coluna de datahora para datetime
        df['datahora'] = pd.to_datetime(df['datahora'])

        # Criar um seletor para escolher múltiplas estações por nome
        opcoes_estacao = sorted(df['nome_estacao'].unique().tolist())
        estacoes_selecionadas = st.multiselect("Selecione as estações", options=opcoes_estacao, default=opcoes_estacao)
        
        # Verificar se DataFrame está vazio após filtragem
        if df.empty:
            st.warning(f"Não há dados para as estações selecionadas no intervalo de tempo.")
            return

        colunas = st.columns(2)

        # Filtrar por estações selecionadas
        if estacoes_selecionadas:
            df = df[df['nome_estacao'].isin(estacoes_selecionadas)]

        for indice, (estacao, nome_estacao) in enumerate(df[['codestacao', 'nome_estacao']].drop_duplicates().values):
            df_estacao = df[df['codestacao'] == estacao]
            df_estacao = df_estacao.sort_values(by='datahora')

            # Verificar se há dados suficientes para plotar
            if not df_estacao.empty:
                ultimo_registro = df_estacao.iloc[-1]
                acc1hr = ultimo_registro['acc1hr']
                acc3hr = ultimo_registro['acc3hr']
                acc6hr = ultimo_registro['acc6hr']
                acc12hr = ultimo_registro['acc12hr']
                acc24hr = ultimo_registro['acc24hr']
                acc48hr = ultimo_registro['acc48hr']
                acc72hr = ultimo_registro['acc72hr']
                acc96hr = ultimo_registro['acc96hr']
                acc120hr = ultimo_registro['acc120hr']
                datahora = ultimo_registro['datahora']

                datahora_ajustada = datahora - timedelta(hours=3)

                # Dados de exemplo, substitua com os valores reais
                dados_chuva = {
                    "Período": ["1h", "3h", "6h", "12h", "24h", "48h", "72h", "96h", "120h"],
                    "Chuva Acumulada (mm)": [acc1hr, acc3hr, acc6hr, acc12hr, acc24hr, acc48hr, acc72hr, acc96hr, acc120hr]
                }

                # Criando um DataFrame
                df_chuva = pd.DataFrame(dados_chuva)

                # Adicionando uma coluna auxiliar para ordenação correta
                df_chuva["Duração (h)"] = [1, 3, 6, 12, 24, 48, 72, 96, 120]

                # Ordenando o DataFrame pela coluna auxiliar de forma decrescente
                df_chuva = df_chuva.sort_values(by="Duração (h)", ascending=False)

                # Removendo a coluna auxiliar, pois ela não é mais necessária
                df_chuva = df_chuva.drop(columns=["Duração (h)"])

                # Criando o gráfico de linha com Plotly
                fig = px.line(df_chuva, x="Período", y="Chuva Acumulada (mm)", title=f"Estação: {nome_estacao} | Última atualização: {datahora_ajustada}")
                fig.update_xaxes(categoryorder='array', categoryarray=["120h","96h", "72h", "48h", "24h", "12h", "6h", "3h", "1h"])

                # Atualizar o layout do gráfico para usar widthImage como largura
                fig.update_layout(width=widthImage*0.5)

                # Usar a coluna correspondente para esta estação
                with colunas[indice % 2]:
                    st.plotly_chart(fig, use_container_width=False)
            else:
                with colunas[indice % 2]:  # Ajuste para evitar erro se houver mais de 2 estações
                    st.warning(f"Não há dados suficientes para a estação: {nome_estacao}")
    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
        return