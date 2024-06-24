import streamlit as st
from src.page1.mapa import cards_informativo
from src.page1.matriz import grafico_heatmap
from src.utils.tamanho_tela import tamanho_tela
from src.utils.auto_refresh import atualizarPage


def gatilhos_hidro():
    
    atualizarPage()
    
    cards_informativo()
    grafico_heatmap()
    
