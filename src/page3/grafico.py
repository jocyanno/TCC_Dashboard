import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

def graficoAlagamentoseDeslizamentos():
    piedade = [-8.1128, -35.0150]
    socorro = [-8.1089, -34.9844]

    data = [
        (*piedade, 1.5),
        (*socorro, 2.0), 
    ]

    mapa = folium.Map(location=[-8.1128, -35.0150], zoom_start=13)

    HeatMap(data).add_to(mapa)

    folium_static(mapa)