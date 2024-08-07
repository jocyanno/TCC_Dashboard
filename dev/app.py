import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from src.pag.gatilhos_hidro import gatilhos_hidro
from src.pag.monitoramento_real import monitoramento_real
from src.pag.visao_historica import visao_historica
from src.pag.tendencia_apac import tendencia_apac
from src.pag.registro_ocorrencias import registro_ocorrencias

favicon = Image.open("src/assets/favicon.jpg")

st.set_page_config(page_title="TCC Jocyanno", layout="wide", page_icon=favicon)

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=[
            "Gatilhos Hidro",
            "Monitoramento Em Tempo Real",
            "Histórico Chuva Por Região",
            "Tendência da APAC",
            "Registro de Ocorrências",
        ],
        icons=["patch-exclamation", "r-circle-fill", "reception-4"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Gatilhos Hidro":
    gatilhos_hidro()
if selected == "Monitoramento Em Tempo Real":
    monitoramento_real()
if selected == "Histórico Chuva Por Região":
    visao_historica()
if selected == "Tendência da APAC":
    tendencia_apac()
if selected == "Registro de Ocorrências":
    registro_ocorrencias()
