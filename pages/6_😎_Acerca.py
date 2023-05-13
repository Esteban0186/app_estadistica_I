import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
import base64
from Principal import df

#Descargar script

def link_descarga(ruta, nombre):
    with open(ruta, 'rb') as f:
        archivo = f.read()
        st.markdown(f'<a href="data:application/octet-stream;base64,{base64.b64encode(archivo).decode("utf-8")}" download="{nombre}">Descarga Script de R</a>', unsafe_allow_html=True)



#Descagar html

ruta_html = "data/script_R.html"
nombre_html = 'script_R.html'

#Descargador de Archivos

class descargador_archivos():
#Cadena de texto para el descargador

     def __init__(self, data, nombre_archivo = "mi_archivo", extension_archivo = "txt"):
          super(descargador_archivos, self).__init__()
          self.data = data
          self.nombre_archivo = nombre_archivo
          self.extension_archivo = extension_archivo

     def descargar(self):
          b64 = base64.b64encode(self.data.encode()).decode()
          nuevo_nombre_archivo = "{}.{}".format(self.nombre_archivo, self.extension_archivo)
          href = f'<a href="data:file/{self.extension_archivo};base64,{b64}" download="{nuevo_nombre_archivo}">Descarga Base de Datos</a>' 
          st.markdown(href, unsafe_allow_html = True)

colored_header(
    label="Acerca",
    description="""Aplicación realizada por el Grupo 2 del curso Estadística Introductoria I,
                    Universidad de Costa Rica""",
    color_name="orange-40")
st.subheader("Integrantes")
st.markdown("* Malcom")
st.markdown("* Lucía")
st.markdown("* Nayelli")
st.markdown("* David")
st.markdown("* Esteban")

st.subheader("Descargar datos en csv")

df_csv = df

csv = df.to_csv(index = False)


st.download_button("Descargar base de datos",
                   data = csv,
                   file_name= "Base_datos.csv",
                   mime = "text/csv")

descargador_archivos(df_csv.to_csv(), nombre_archivo="Mundial", extension_archivo= "txt").descargar()

link_descarga(ruta=ruta_html, nombre=nombre_html)

st.balloons()

rain(
    emoji="😎",
    font_size=54,
    falling_speed=5,
    animation_length="infinite")

if st.button("Ir a Página Principal"):
    switch_page("Principal")