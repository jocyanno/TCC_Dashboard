import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
from branca.colormap import LinearColormap


def criacao_mapa():

    piedade = [-8.1128, -35.0150]
    socorro = [-8.1089, -34.9844]

    data = [
        (*piedade, 1.5),
        (*socorro, 2.0),
    ]

    mapa = folium.Map(location=[-8.1128, -35.0150], zoom_start=13)

    HeatMap(data).add_to(mapa)

    # Cria um mapa de cores
    colormap = LinearColormap(["green", "yellow", "red"], vmin=1.0, vmax=2.0)

    # Adiciona o mapa de cores como uma legenda
    colormap.caption = "Intensidade da chuva"
    colormap.add_to(mapa)

    # Adiciona um marcador ao mapa
    folium.Marker(
        location=[-8.1128, -35.0150],
        popup=folium.Popup(
            "Último registro: 1.5 mm <br> Data: 05/01/2024 13:35:54", max_width=200
        ),
    ).add_to(mapa)
    folium.Marker(
        location=[-8.1089, -34.9844],
        popup=folium.Popup(
            "Último registro: 2.0 mm <br> Data: 05/01/2024 14:05:22", max_width=200
        ),
    ).add_to(mapa)

    folium_static(mapa)
