import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
import base64
from Principal import df

#Descargar script
@st.cache_data
def link_descarga(ruta, nombre):
    with open(ruta, 'rb') as f:
        archivo = f.read()
        st.markdown(f'<a href="data:application/octet-stream;base64,{base64.b64encode(archivo).decode("utf-8")}" download="{nombre}">Descarga Script de R</a>', unsafe_allow_html=True)



#Descagar html

ruta_html = "data/script_R.html"
nombre_html = 'script_R.html'

colored_header(
    label="Acerca",
    description="""Aplicación realizada por el Grupo 2 del curso Estadística Introductoria I,
                    Universidad de Costa Rica""",
    color_name="orange-40")
st.subheader("Integrantes")
st.markdown("* Malcom Morris")
st.markdown("* Lucía Carvajal")
st.markdown("* Nayelli Cabezas")
st.markdown("* David Mora")
st.markdown("* Esteban Navarro")

st.subheader("Descargar datos en csv")

df_csv = df

csv = df.to_csv(index = False)


st.download_button("Descargar base de datos",
                   data = csv,
                   file_name= "Base_datos.csv",
                   mime = "text/csv")


link_descarga(ruta=ruta_html, nombre=nombre_html)

st.balloons()

rain(
    emoji="😎",
    font_size=54,
    falling_speed=5,
    animation_length="infinite")

if st.button("Ir a Página Principal"):
    switch_page("Principal")