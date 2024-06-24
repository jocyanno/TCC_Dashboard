import datetime
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

def graficoAlagamentoseDeslizamentos(widthImage):
    st.title("Histórico Chuva Por Região")
    
    # Dicionário mapeando regiões aos nomes dos arquivos
    arquivos_por_regiao = {
        "Barra de Jangada": "Barra_de_Jangada_Calculado.csv",
        "Cajueiro Seco": "Cajueiro_Seco_Calculado.csv",
        "Cavaleiro": "Cavaleiro_Calculado.csv",
        "CavaleiroII": "Cavaleiro2_Calculado.csv",
        "Centro": "Centro_Calculado.csv",
        "CuradoII": "CuradoII_Calculado.csv",
        "Muribeca": "Muribeca_Calculado.csv",
        "Piedade": "Piedade_Calculado.csv",
        "Prazeres": "Prazeres_Calculado.csv",
        "Socorro": "Socorro_Calculado.csv",
    }

    # Seleção da região
    regiao = st.selectbox(
        "Selecione a região", options=["Todas"] + sorted(arquivos_por_regiao.keys())
    )

    if regiao == "Todas":
        # Exibir gráficos para todas as regiões sem filtragem por data
        st.subheader("Gráficos para Todas as Regiões")
        for reg, arquivo in arquivos_por_regiao.items():
            caminho_do_arquivo = rf'C:\Users\Jocya\OneDrive\Documents\TCC\Projeto_TCC\dev\src\page3\estacoes\{arquivo}'
            dados = pd.read_csv(caminho_do_arquivo, delimiter=',', decimal=',')

            st.subheader(f"Região: {reg}")

            # Exibir os 5 gráficos diferentes
            for coluna in ['chuva_24h', 'chuva_3d', 'chuva_6d', 'chuva_7d', 'chuva_15d']:
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=dados['datahora'], y=dados[coluna], mode='lines', name=coluna))
                fig.update_layout(title=f"Gráfico de {coluna} para {reg}", xaxis_title='Data', yaxis_title=coluna, width=widthImage)
                st.plotly_chart(fig)

    else:
        # Construção do caminho do arquivo com base na região selecionada
        nome_do_arquivo = arquivos_por_regiao[regiao]
        caminho_do_arquivo = rf'C:\Users\Jocya\OneDrive\Documents\TCC\Projeto_TCC\dev\src\page3\estacoes\{nome_do_arquivo}'

        # Leitura do arquivo
        dados = pd.read_csv(caminho_do_arquivo, delimiter=',', decimal=',')

        # Conversão das datas no DataFrame
        dados['datahora'] = pd.to_datetime(dados['datahora'], format='%Y-%m-%d')
        
        # Definir datas mínimas e máximas do CSV para os seletores de data
        data_min = dados['datahora'].min().date()
        data_max = dados['datahora'].max().date()

        # Filtragem por data
        start_date = st.date_input('Data de início', data_min, min_value=data_min, max_value=data_max)
        end_date = st.date_input('Data de término', data_max, min_value=data_min, max_value=data_max)
        
        st.subheader(f"Gráfico para a Região: {regiao}")
        
        # Aplicar filtragem
        mask = (dados['datahora'] >= pd.Timestamp(start_date)) & (dados['datahora'] <= pd.Timestamp(end_date))
        dados_filtrados = dados.loc[mask]

        # Exibir os 5 gráficos diferentes para a região filtrada
        for coluna in ['chuva_24h', 'chuva_3d', 'chuva_6d', 'chuva_7d', 'chuva_15d']:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dados_filtrados['datahora'], y=dados_filtrados[coluna], mode='lines', name=coluna))
            fig.update_layout(title=f"Gráfico de {coluna} para {regiao}", xaxis_title='Data', yaxis_title=coluna, width=widthImage)
            st.plotly_chart(fig)