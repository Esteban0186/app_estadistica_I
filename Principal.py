#Paquetes

import streamlit as st
from  PIL import Image
from streamlit_extras.colored_header import colored_header
import pandas as pd

#Objetos precargados

img = Image.open("data/football.png")

st.set_page_config(page_title = "Trabajo final",
                   page_icon = img,
                   layout = "wide", #Inciar con las imagenes a lo ancho
                   initial_sidebar_state = "expanded")

@st.cache_data
def cargar_datos():
       df = pd.read_csv("data/datos_limpios.csv")
       return df

df = cargar_datos()

malos  = ["Ã<81>", "Ã©", "Ã¡", "Ã³", "Ã", "Ã±", "Ã³Åº", "í\u0081", "íº", "Åº", "Å‚", "Å„", "¯", "í®", "í¢", "í¸", "í«", "í±", "¼", "Å«", "Ä‡", "Å¡", "Ä†", "ÄŒ", "§", "í‰", "£", "Ä™", "Ä…", "Å\u0081", "í“", "Å i", "Ä\u008d", "Ä\u0090", "Å½", "¦", "í¨", "í¤", "Ä°", "ÄŸ", "í´","Ã±Ã¡", "Ã", "í“"]
buenos = ["Á", "é", "á", "ó", "í", "ñ", "ó", "Á", "ú", "z", "l", "ń", "ï", "î", "â", "ø", "ë", "ñ", "z", "ū", "ć", "š", "Ć", "Č", "ç", "É", "ã", "ę", "ą", "Ł", "Ó", "Ši", "č", "Đ", "Ž", "æ", "e", "ä", "İ", "ğ", "ô", "ñ", "Á", "Ó"]

#Limpiar los datos

def limpiar_nombres(data_frame= None, variable = "", correccion = None, error = None):
      df = data_frame
      df[variable] = df[variable].str.replace("|".join(error), lambda x: correccion[error.index(x.group(0))], regex=True)

      return df

df = limpiar_nombres(data_frame= df, variable = "Jugador",
                     error =malos, correccion = buenos)

#Estilo de la página

def main():
       st.title("Trabajo Final: Datos del Mundial")

       colored_header(
                label="Introducción",
                description="""El fútbol ha evolucionado desde sus inicios como una actividad social y lúdica en el siglo XIX hasta convertirse en la principal actividad deportiva en muchos países. En sus primeros años, el fútbol era jugado por obreros de diferentes industrias, lo que generaba una identificación social y urbana más que una identidad partidista. Sin embargo, en la actualidad, el fútbol ha adquirido una trascendencia global y los clubes se han convertido en marcas comerciales (López-Herraiz, 2021). Se busca tener equipos competitivos, contar con los mejores jugadores y disfrutar de los beneficios mediáticos, sociales y económicos que esto conlleva.
Así, el propósito de este trabajo es realizar un análisis detallado y presentar datos relevantes y estadísticas relacionadas con el desempeño de los equipos y jugadores destacados durante el Mundial de Fútbol de Qatar 2022. La realización de este trabajo de estadística es una oportunidad para comprender los patrones y tendencias en el rendimiento de los equipos participantes en el Mundial de Fútbol de Qatar 2022. A través de este análisis, se examina el desempeño de los equipos y se identifican los factores clave que contribuyen al éxito de un equipo en este tipo de competición (Merrell, 2023).
Para lograr esto, se hará énfasis en variables clave del jugador como la posición en la que juega, la confederación a la que pertenece, los minutos jugados, los goles y las tarjetas amarillas.
Se identifican correlaciones entre variables, como la relación entre la posición de un equipo en el torneo y su desempeño en términos de minutos jugados, goles marcados y tarjetas amarillas. Lo anterior, brinda información valiosa sobre los factores que pueden tener un impacto significativo en el éxito de un equipo en el Mundial. 
Estos datos permiten analizar el rendimiento de las confederaciones en el torneo, identificar a las posiciones más destacadas y evaluar su contribución al éxito de sus equipos.
""",
                color_name="red-40")




if __name__ == '__main__':
	main()