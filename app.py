import streamlit as st
from streamlit_option_menu import option_menu
from src.pag.gatilhos_hidro import gatilhos_hidro
from src.pag.monitoramento_real import monitoramento_real
from src.pag.visao_historica import visao_historica

st.set_page_config(layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Gatilhos Hidro", "Monitoramento Real", "Visão Histórica"],
        icons=["patch-exclamation", "r-circle-fill", "reception-4"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Gatilhos Hidro":
    gatilhos_hidro()
if selected == "Monitoramento Real":
    monitoramento_real()
if selected == "Visão Histórica":
    visao_historica()
