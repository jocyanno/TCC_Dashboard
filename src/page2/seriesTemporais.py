import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from src.utils.tamanho_tela import tamanho_tela

def series_temporais(widthImage):
  # Suponha que temos o seguinte DataFrame
  data = pd.DataFrame(
    {
      "data": pd.date_range(start="1/1/2022", periods=100),
      "Piedade": np.random.randint(1, 20, 100),
      "Socorro": np.random.randint(1, 20, 100),
      "Muribeca": np.random.randint(1, 20, 100),
    }
  )

  # Selecionando a região
  regiao = st.selectbox(
    "Selecione a região", options=["Todas", "Piedade", "Socorro", "Muribeca"]
  )

  if regiao == "Todas":
    for reg in data.columns[1:]:
      # Criando o gráfico de séries temporais para cada região
      fig = px.line(data, x="data", y=reg)
      # Adicionando a legenda ao eixo y
      fig.update_yaxes(title_text="Milimetros de chuva (mm)")
      fig.update_layout(width=widthImage)
      # Exibindo o título do gráfico
      st.header(reg)
      st.plotly_chart(fig)
  else:
    # Criando o gráfico de séries temporais para a região selecionada
    fig = px.line(data, x="data", y=regiao)
    st.markdown(f"### {regiao}")
    # Adicionando a legenda ao eixo y
    fig.update_yaxes(title_text="Milimetros de chuva (mm)")
    fig.update_layout(width=widthImage)
    # Exibindo o gráfico
    st.plotly_chart(fig)