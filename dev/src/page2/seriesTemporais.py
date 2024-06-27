import pandas as pd
import streamlit as st
from config_db import consultar_estacoes_disponiveis_e_ultimos_registros
from datetime import timedelta
import plotly.express as px
from src.utils.auto_refresh import atualizarPage

def series_temporais(widthImage):
    try:
        st.title("Monitoramento Em Tempo Real")
        
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

        # Filtrar por estações selecionadas
        if estacoes_selecionadas:
            df = df[df['nome_estacao'].isin(estacoes_selecionadas)]
        
        # Verificar se DataFrame está vazio após filtragem
        if df.empty:
            st.warning(f"Não há dados para as estações selecionadas no intervalo de tempo.")
            return

        # Criar uma lista de períodos e a respectiva coluna no DataFrame
        periodos = ["acc1hr", "acc3hr", "acc6hr", "acc12hr", "acc24hr", "acc48hr", "acc72hr", "acc96hr", "acc120hr"]
        periodos_legendas = ["-1h", "-3h", "-6h", "-12h", "-24h", "-48h", "-72h", "-96h", "-120h"]

        # Criar um DataFrame para o heatmap
        heatmap_data = {
            "Estacao": [],
            "Periodo": [],
            "Chuva Acumulada (mm)": [],
            "DataHora": []
        }

        for estacao, nome_estacao in df[['codestacao', 'nome_estacao']].drop_duplicates().values:
            df_estacao = df[df['codestacao'] == estacao]
            df_estacao = df_estacao.sort_values(by='datahora')

            # Verificar se há dados suficientes para plotar
            if not df_estacao.empty:
                ultimo_registro = df_estacao.iloc[-1]

                for periodo, legenda in zip(periodos, periodos_legendas):
                    heatmap_data["Estacao"].append(nome_estacao)
                    heatmap_data["Periodo"].append(legenda)
                    # Substituir NaN por 0
                    valor_chuva = ultimo_registro[periodo] if pd.notna(ultimo_registro[periodo]) else 0
                    heatmap_data["Chuva Acumulada (mm)"].append(valor_chuva)
                    # Subtrair 3 horas do horário UTC e formatar a data e hora para o padrão brasileiro e 24 horas
                    datahora_ajustada = ultimo_registro['datahora'] - timedelta(hours=3)
                    heatmap_data["DataHora"].append(datahora_ajustada.strftime("%d/%m/%Y %H:%M"))

        # Criar um DataFrame a partir dos dados do heatmap
        df_heatmap = pd.DataFrame(heatmap_data)

        # Ordenar o DataFrame para garantir a ordem correta dos períodos
        df_heatmap["Periodo"] = pd.Categorical(df_heatmap["Periodo"], categories=periodos_legendas[::-1], ordered=True)

        # Criar a tabela pivô para o heatmap
        df_pivot = df_heatmap.pivot_table(index="Estacao", columns="Periodo", values="Chuva Acumulada (mm)", aggfunc='mean').fillna(0)
        
        # Adicionar a coluna DataHora ao DataFrame pivô
        df_pivot_hover = df_heatmap.pivot_table(index="Estacao", columns="Periodo", values="DataHora", aggfunc=lambda x: x)

        # Definir altura e largura do gráfico
        altura_grafico = widthImage * 0.3 # Utilize a largura especificada pela função
        largura_grafico = widthImage # Ajuste a altura conforme necessário

        # Criar o heatmap com Plotly
        fig = px.imshow(df_pivot,
                        labels=dict(x="Período", y="Estação", color="Chuva Acumulada (mm)"),
                        x=df_pivot.columns,
                        y=df_pivot.index,
                        text_auto=True,  # Adicionar valores no heatmap
                        aspect="auto")  # Para ajustar a proporção do heatmap

        # Atualizar o layout do gráfico para definir altura e largura
        fig.update_layout(width=largura_grafico, height=altura_grafico)

        # Adicionar dados de hover personalizados
        hovertemplate = "Período: %{x}<br>Estação: %{y}<br>Chuva Acumulada: %{z} mm<br>DataHora: %{customdata}"
        fig.update_traces(hovertemplate=hovertemplate, customdata=df_pivot_hover.values)

        # Exibir o heatmap
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
        return