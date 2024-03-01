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
    np.random.shuffle(datas)

    if regiao == "Todas":
        for reg, (chuva_mm, deslizamentos) in dados.items():

            plot = go.Figure(
                data=[
                    go.Scatter(
                        x=chuva_mm,
                        y=deslizamentos,
                        mode="markers",
                        marker=dict(
                            color=deslizamentos, size=deslizamentos, showscale=True
                        ),
                        text=datas,
                        hovertemplate="<b>Data:</b> %{text}<br>"
                        + "<b>Chuva (mm):</b> %{x}<br>"
                        + "<b>Deslizamentos:</b> %{y}<br>",
                    )
                ]
            )
            plot.update_xaxes(title_text="Chuva em mm")
            plot.update_yaxes(title_text="Quantidade de Deslizamentos")
            plot.update_layout(width=widthImage)
            st.header(reg)
            st.plotly_chart(plot)
    else:
        chuva_mm, deslizamentos = dados[regiao]
        plot = go.Figure(
            data=[
                go.Scatter(
                    x=chuva_mm,
                    y=deslizamentos,
                    mode="markers",
                    marker=dict(
                        color=deslizamentos, size=deslizamentos, showscale=True
                    ),
                    text=datas,
                    hovertemplate="<b>Data:</b> %{text}<br>"
                    + "<b>Chuva (mm):</b> %{x}<br>"
                    + "<b>Deslizamentos:</b> %{y}<br>",
                )
            ]
        )

        plot.update_xaxes(title_text="Chuva em mm")
        plot.update_yaxes(title_text="Quantidade de Deslizamentos")
        plot.update_layout(width=widthImage)
        st.header(regiao)
        st.plotly_chart(plot)
