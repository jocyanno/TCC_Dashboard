import streamlit as st
from config_db_Apac import consultar_ultimo_registro_tendencia_grafico
import pandas as pd
from src.utils.tamanho_tela import tamanho_tela

def cor_linha(metropolitana):
    # Define a cor com base na nomenclatura do argumento "Metropolitana"
    if metropolitana == 'Sem chuva':
        return 'background-color: gray'
    elif metropolitana == 'Fraca':
        return 'background-color: darkgray'
    elif metropolitana == 'Fraca a moderada':
        return 'background-color: lightblue'
    elif metropolitana == 'Moderada':
        return 'background-color: yellow'
    elif metropolitana == 'Moderada a forte':
        return 'background-color: orange'
    elif metropolitana == 'Forte':
        return 'background-color: red'
    else:
        return 'background-color: white'

def aplicar_cor(row):
    # Aplica a cor de fundo apenas à coluna "Metropolitana"
    cor = cor_linha(row['Metropolitana'])
    return [cor] * len(row)

def tendencia_apac():
    widthImage = tamanho_tela()
    st.title("Tendência da APAC")
    
    # Consultar dados do banco de dados
    dados = consultar_ultimo_registro_tendencia_grafico()

    # Criar um DataFrame para exibição, sem a coluna ID
    colunas = ['Data', 'Metropolitana', 'Mínima (mm)', 'Máxima (mm)']
    df = pd.DataFrame(dados, columns=colunas)

    # Aplicar a coloração às linhas
    styled_df = df.style.apply(aplicar_cor, axis=1)

    # Exibir tabela no Streamlit com estilização
    st.dataframe(styled_df, width=widthImage)