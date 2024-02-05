import streamlit as st
from src.page3.grafico import graficoAlagamentoseDeslizamentos


def visao_historica():

    st.markdown("### Histórico Alagamento e Deslizamentos")
    col1, col2 = st.columns(2)

    # Seletores de data
    start_date = col1.date_input("Data inicial")
    end_date = col2.date_input("Data Final")
    
    graficoAlagamentoseDeslizamentos()
