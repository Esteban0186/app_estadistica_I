#Paquetes

import streamlit as st
from  PIL import Image
from streamlit_extras.colored_header import colored_header
import pandas as pd
import base64


#Objetos precargados

img = Image.open("data/football.png")

df = pd.read_csv("data/datos_limpios.csv")

malos  = ["Ã<81>", "Ã©", "Ã¡", "Ã³", "Ã", "Ã±", "Ã³Åº", "í\u0081", "íº", "Åº", "Å‚", "Å„", "¯", "í®", "í¢", "í¸", "í«", "í±", "¼", "Å«", "Ä‡", "Å¡", "Ä†", "ÄŒ", "§", "í‰", "£", "Ä™", "Ä…", "Å\u0081", "í“", "Å i", "Ä\u008d", "Ä\u0090", "Å½", "¦", "í¨", "í¤", "Ä°", "ÄŸ", "í´","Ã±Ã¡", "Ã"]
buenos = ["Á", "é", "á", "ó", "í", "ñ", "ó", "Á", "ú", "z", "l", "ń", "ï", "î", "â", "ø", "ë", "ñ", "z", "ū", "ć", "š", "Ć", "Č", "ç", "É", "ã", "ę", "ą", "Ł", "Ó", "Ši", "č", "Đ", "Ž", "æ", "e", "ä", "İ", "ğ", "ô", "ñ", "Á"]

#Limpiar los datos

def limpiar_nombres(data_frame= None, variable = "", correccion = None, error = None):
      df = data_frame
      df[variable] = df[variable].str.replace("|".join(error), lambda x: correccion[error.index(x.group(0))], regex=True)

      return df

df = limpiar_nombres(data_frame= df, variable = "Jugador",
                     error =malos, correccion = buenos)

#Descagar html

ruta_html = "data/script_R.html"
nombre_html = 'script_R.html'

def link_descarga(ruta, nombre):
    with open(ruta, 'rb') as f:
        archivo = f.read()
        st.markdown(f'<a href="data:application/octet-stream;base64,{base64.b64encode(archivo).decode("utf-8")}" download="{nombre}">Descarga Script de R</a>', unsafe_allow_html=True)


#Estilo de la página

st.set_page_config(page_title = "Trabajo final",
                   page_icon = img,
                   layout = "wide", #Inciar con las imagenes a lo ancho
                   initial_sidebar_state = "expanded")


def main():
       st.title("Trabajo Final: Datos del Mundial")

       colored_header(
                label="Intro",
                description="Descripción",
                color_name="red-40")
       link_descarga(ruta=ruta_html, nombre=nombre_html)




if __name__ == '__main__':
	main()