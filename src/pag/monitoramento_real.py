import streamlit as st
from src.page2.grafico_heatmap import grafico_heatmap_page2
from src.page2.seriesTemporais import series_temporais


def monitoramento_real():
    st.markdown("### Monitoramento Real")
    grafico_heatmap_page2()
    series_temporais()
