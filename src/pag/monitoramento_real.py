import streamlit as st
from src.page2.grafico_heatmap import grafico_heatmap_page2
from src.page2.seriesTemporais import series_temporais
from src.utils.tamanho_tela import tamanho_tela


def monitoramento_real():
    st.markdown("### Monitoramento Real")
    
    widthImage = tamanho_tela()
    
    grafico_heatmap_page2(widthImage)
    series_temporais(widthImage)
