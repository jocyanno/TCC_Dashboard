# import folium
# from streamlit_folium import folium_static
# from folium.plugins import HeatMap
# from branca.colormap import LinearColormap
import streamlit as st
from config_db import consultar_ultimo_registro_estacao
from datetime import timedelta

def cards_informativo():
  
    st.title("Gatilhos Hidrometeorologicos Piedade")
    
    dados  = consultar_ultimo_registro_estacao('260790106A')
    
    (id, val_120h, val_12h, val_1h, val_24h, val_3h, val_48h, val_6h, val_72h, val_96h, estacao, codigo, data_hora, outro_valor, local) = dados
    
    data_hora_ajustada = data_hora - timedelta(hours=3)
    
    # Cria três colunas com larguras iguais
    col1, col2, col3 = st.columns(3)
    
    with col1:
      st.markdown(
        """
        <div style="
          margin-bottom: 10px;
          border: 2px solid #000;
          border-radius: 5px;
          background-color: #292929;
          width: 100%;
          height: auto;
          padding: 10px;
          text-align: center;
        ">
        <h3 style="color: #FFFFFF;">Registro Últimas 24h</h3>
        <h3 style="color: #2EB2FF; font-size: 40px">{:.2f} mm</h3>
        <h5 style="color: #FFFFFF;">Última Leitura: {}</h5>
        </div>
        """.format(
          val_24h,
          data_hora_ajustada.strftime('%Y-%m-%d %H:%M:%S'),
        ),
        unsafe_allow_html=True,
      )
    
    with col2:
      st.markdown(
        """
        <div style="
          margin-bottom: 10px;
          border: 2px solid #000;
          border-radius: 5px;
          background-color: #292929;
          width: 100%;
          height: auto;
          padding: 10px;
          text-align: center;
        ">
        <h3 style="color: #FFFFFF;">Registro Últimas 48h</h3>
        <h3 style="color: #2EB2FF; font-size: 40px">{:.2f} mm</h3>
        <h5 style="color: #FFFFFF;">Última Leitura: {}</h5>
        </div>
        """.format(
          val_48h,
          data_hora_ajustada.strftime('%Y-%m-%d %H:%M:%S'),
        ),
        unsafe_allow_html=True,
      )
    
    with col3:
      st.markdown(
        """
        <div style="
          margin-bottom: 10px;
          border: 2px solid #000;
          border-radius: 5px;
          background-color: #292929;
          width: 100%;
          height: auto;
          padding: 10px;
          text-align: center;
        ">
        <h3 style="color: #FFFFFF;">Registro Últimas 120h</h3>
        <h3 style="color: #2EB2FF; font-size: 40px">{:.2f} mm</h3>
        <h5 style="color: #FFFFFF;">Última Leitura: {}</h5>
        </div>
        """.format(
          val_120h,
          data_hora_ajustada.strftime('%Y-%m-%d %H:%M:%S'),
        ),
        unsafe_allow_html=True,
      )


    # piedade = [-8.1128, -35.0150]
    # socorro = [-8.1089, -34.9844]

    # data = [
    #     (*piedade, 1.5),
    #     (*socorro, 2.0),
    # ]

    # mapa = folium.Map(location=[-8.1128, -35.0150], zoom_start=13)

    # HeatMap(data, gradient={0.5: 'yellow', 1: 'red'}).add_to(mapa)

    # # Cria um mapa de cores
    # colormap = LinearColormap(["green", "yellow", "red"], vmin=1.0, vmax=2.0)

    # # Adiciona o mapa de cores como uma legenda
    # colormap.caption = "Intensidade da chuva"
    # colormap.add_to(mapa)

    # # Adiciona um marcador ao mapa
    # folium.Marker(
    #     location=[-8.1128, -35.0150],
    #     popup=folium.Popup(
    #         "Último registro: 1.5 mm <br> Data: 05/01/2024 13:35:54", max_width=200
    #     ),
    # ).add_to(mapa)
    # folium.Marker(
    #     location=[-8.1089, -34.9844],
    #     popup=folium.Popup(
    #         "Último registro: 2.0 mm <br> Data: 05/01/2024 14:05:22", max_width=200
    #     ),
    # ).add_to(mapa)

    # folium_static(mapa, width=widthImage, height=400)
