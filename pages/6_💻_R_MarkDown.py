import streamlit as st 
from streamlit_extras.colored_header import colored_header
import streamlit.components.v1 as components
import base64

#Descagar html

ruta_html = "data/script_R.html"
nombre_html = 'script_R.html'

def link_descarga(ruta, nombre):
    with open(ruta, 'rb') as f:
        archivo = f.read()
        st.markdown(f'<a href="data:application/octet-stream;base64,{base64.b64encode(archivo).decode("utf-8")}" download="{nombre}">Descarga Script de R</a>', unsafe_allow_html=True)



colored_header(
    label="Descarga el escritp de R Mark Down",
    description="""Descripción""",
    color_name="orange-40")


iframe = components.iframe(src="data/script_R.html", width=700, height=500)

st.write(iframe)

link_descarga(ruta= ruta_html, nombre= nombre_html)