import datetime
import plotly.graph_objects as px
import numpy as np
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def graficoAlagamentoseDeslizamentos(widthImage):

    regiao = st.selectbox(
        "Selecione a região", options=["Todas", "Piedade", "Socorro", "Muribeca"]
    )

    np.random.seed(42)
    dados = {
        "Piedade": (np.random.randint(1, 101, 100), np.random.randint(1, 101, 100)),
        "Socorro": (np.random.randint(1, 101, 100), np.random.randint(1, 101, 100)),
        "Muribeca": (np.random.randint(1, 101, 100), np.random.randint(1, 101, 100)),
    }

    datas = pd.date_range(start="1/1/2020", periods=100).to_pydatetime().tolist()
    datas.sort()

    # Seletor de tempo
    tempo = st.date_input(
        "Selecione o intervalo de tempo", [datas[0].date(), datetime.date(2020, 12, 31)]
    )

    # Converte o tempo diretamente em objetos de data
    inicio = pd.to_datetime(tempo[0])
    fim = pd.to_datetime(tempo[1])

    try:
        mask = (np.array(datas) >= inicio) & (np.array(datas) <= fim)
        datas_filtradas = np.array(datas)[mask]
    except ValueError as e:
        st.error("Não foram encontrados dados para a data selecionada.")
        return

    if regiao == "Todas":
        for reg, (chuva_mm, deslizamentos) in dados.items():
            plot_chuva = go.Figure()

            plot_chuva.add_trace(
                go.Scatter(
                    x=datas_filtradas,
                    y=chuva_mm,
                    mode="lines",
                    name="Chuva em mm",
                    hovertemplate="<b>Data:</b> %{x}<br>"
                    + "<b>Chuva (mm):</b> %{y}<br>",
                )
            )

            plot_chuva.update_xaxes(title_text="Data")
            plot_chuva.update_yaxes(title_text="Chuva em mm")
            plot_chuva.update_layout(width=widthImage, template="plotly_white")
            st.header(f"Chuva em mm - {reg}")
            st.plotly_chart(plot_chuva)

            plot_deslizamentos = go.Figure()

            plot_deslizamentos.add_trace(
                go.Scatter(
                    x=datas_filtradas,
                    y=deslizamentos,
                    mode="lines",
                    name="Deslizamentos",
                    hovertemplate="<b>Data:</b> %{x}<br>"
                    + "<b>Deslizamentos:</b> %{y}<br>",
                )
            )

            plot_deslizamentos.update_xaxes(title_text="Data")
            plot_deslizamentos.update_yaxes(title_text="Deslizamentos")
            plot_deslizamentos.update_layout(width=widthImage, template="plotly_white")
            st.header(f"Deslizamentos - {reg}")
            st.plotly_chart(plot_deslizamentos)
    else:
        chuva_mm, deslizamentos = dados[regiao]

        plot_chuva = go.Figure()

        plot_chuva.add_trace(
            go.Scatter(
                x=datas_filtradas,
                y=chuva_mm,
                mode="lines",
                name="Chuva em mm",
                hovertemplate="<b>Data:</b> %{x}<br>" + "<b>Chuva (mm):</b> %{y}<br>",
            )
        )

        plot_chuva.update_xaxes(title_text="Data")
        plot_chuva.update_yaxes(title_text="Chuva em mm")
        plot_chuva.update_layout(width=widthImage, template="plotly_white")
        st.header(f"Chuva em mm - {regiao}")
        st.plotly_chart(plot_chuva)

        plot_deslizamentos = go.Figure()

        plot_deslizamentos.add_trace(
            go.Scatter(
                x=datas_filtradas,
                y=deslizamentos,
                mode="lines",
                name="Deslizamentos",
                hovertemplate="<b>Data:</b> %{x}<br>"
                + "<b>Deslizamentos:</b> %{y}<br>",
            )
        )

        plot_deslizamentos.update_xaxes(title_text="Data")
        plot_deslizamentos.update_yaxes(title_text="Deslizamentos")
        plot_deslizamentos.update_layout(width=widthImage, template="plotly_white")
        st.header(f"Deslizamentos - {regiao}")
        st.plotly_chart(plot_deslizamentos)
