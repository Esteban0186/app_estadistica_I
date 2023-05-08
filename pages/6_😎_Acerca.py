import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
import base64
from Principal import df

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
descarga = descargador_archivos(df_csv.to_csv(), nombre_archivo="Mundial", extension_archivo= "txt").descargar()

st.balloons()

rain(
    emoji="😎",
    font_size=54,
    falling_speed=5,
    animation_length="infinite")
