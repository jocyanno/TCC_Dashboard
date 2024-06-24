import folium
from streamlit_folium import components, folium_static
from folium.plugins import HeatMap

def graficoAlagamentoseDeslizamentos(widthImage):
    piedade = [-8.1128, -35.0150]
    socorro = [-8.1089, -34.9844]

    data = [
        (*piedade, 1.5),
        (*socorro, 2.0), 
    ]

    mapa = folium.Map(location=[-8.1128, -35.0150], zoom_start=13, width=widthImage)

    HeatMap(data).add_to(mapa)

    # Renderiza o mapa como HTML e exibe-o usando a função components.html
    mapa_html = mapa._repr_html_()
    components.html(mapa_html, width=widthImage, height=widthImage * 0.3)