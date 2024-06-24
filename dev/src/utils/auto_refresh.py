from streamlit_autorefresh import st_autorefresh
import streamlit as st

def atualizarPage():
    
    # Run the autorefresh about every 30000 milliseconds (30 seconds) and stop
    count = st_autorefresh(interval=30000, limit=1440, key="fizzbuzzcounter")
    
    if count == 0:
        st.write("")
    else:
        st.write("")