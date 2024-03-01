import streamlit as st
from src.page1.mapa import criacao_mapa
from src.page1.matriz import grafico_heatmap
from src.utils.tamanho_tela import tamanho_tela


def gatilhos_hidro():

    st.markdown("### Gatilhos Hidrometeorologicos")
    st.write("Selecione a Região desejada:")

    widthImage = tamanho_tela()
    
    criacao_mapa(widthImage)
    grafico_heatmap()
    
