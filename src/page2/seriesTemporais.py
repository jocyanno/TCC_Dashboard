import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

def series_temporais(widthImage):
  try:
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
    
    # Seletor de tempo
    tempo = st.date_input(
        "Selecione o intervalo de tempo", [data['data'].min().date(), data['data'].max().date()]
    )

    # Converte o tempo diretamente em objetos de data
    inicio = pd.to_datetime(tempo[0])
    fim = pd.to_datetime(tempo[1])

  
    mask = (data['data'] >= inicio) & (data['data'] <= fim)
    data_filtrada = data.loc[mask]
  
    if regiao == "Todas":
      for reg in data_filtrada.columns[1:]:
        # Criando o gráfico de séries temporais para cada região
        fig = px.line(data_filtrada, x="data", y=reg)
        # Adicionando a legenda ao eixo y
        fig.update_yaxes(title_text="Milimetros de chuva (mm)")
        fig.update_layout(width=widthImage)
        # Exibindo o título do gráfico
        st.header(reg)
        st.plotly_chart(fig)
    else:
      # Criando o gráfico de séries temporais para a região selecionada
      fig = px.line(data_filtrada, x="data", y=regiao)
      st.markdown(f"### {regiao}")
      # Adicionando a legenda ao eixo y
      fig.update_yaxes(title_text="Milimetros de chuva (mm)")
      fig.update_layout(width=widthImage)
      # Exibindo o gráfico
      st.plotly_chart(fig)
  
  except ValueError as e:
      st.error("Não foram encontrados dados para a data selecionada.")
      return
