import streamlit as st
from src.page1.mapa import criacao_mapa
from src.page1.matriz import grafico_heatmap


def gatilhos_hidro():

    st.markdown("### Gatilhos Hidrometeorologicos")
    st.write("Selecione a Região desejada:")

    criacao_mapa()
    grafico_heatmap()
    
