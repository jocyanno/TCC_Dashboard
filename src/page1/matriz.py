import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def grafico_heatmap():
    st.markdown("### Matriz de Correlação")

    data = {
        "Acumulado": [0.1, 0.2, 0.3],
        "+1 dia Apac": [0.4, 0.5, 0.6],
        "+2 dias Apac": [0.7, 0.8, 0.9],
    }
    df = pd.DataFrame(data, index=["3 dias", "6 dias", "15 dias"])

    cmap = sns.color_palette("RdYlGn_r", as_cmap=True)

    plt.figure(figsize=(6, 3))
    sns.heatmap(df, cmap=cmap, annot=True, cbar_kws={"label": "Risco"})

    plt.text(
        4.5, 2.5, "Baixo Risco", ha="center", va="center", color="g", size="x-large"
    )
    plt.text(
        4.5, 1.5, "Risco Moderado", ha="center", va="center", color="y", size="x-large"
    )
    plt.text(4.5, 0.5, "Alerta", ha="center", va="center", color="r", size="x-large")

    st.pyplot(plt)
