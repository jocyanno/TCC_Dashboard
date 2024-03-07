import streamlit as st
from src.page3.grafico import graficoAlagamentoseDeslizamentos
from src.utils.tamanho_tela import tamanho_tela


def visao_historica():

    st.markdown("### Histórico Deslizamentos e Chuva")
    
    widthImage = tamanho_tela()
    
    graficoAlagamentoseDeslizamentos(widthImage)
