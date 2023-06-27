import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from Principal import df
from st_aggrid import AgGrid
#pip install streamlit-aggrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

colored_header(
                label="Metodología y Base de datos",
                description="""Este estudio se realizó utilizando el software R (R Core Team, 2023), un programa ampliamente reconocido por su capacidad para ejecutar análisis estadísticos. Este software tiene la ventaja de extender sus funciones mediante el uso de paquetes y bibliotecas adicionales, así como a través de la creación de funciones personalizadas. Esto permite realizar una variedad de cálculos y generar gráficos a partir de los datos.

El conjunto de datos utilizado en este análisis proviene directamente del sitio web oficial de la Federación Internacional de Fútbol (FIFA) y se enfoca específicamente en la Copa Mundial de Qatar 2022 (FIFA, 2023). La población de estudio abarca la totalidad de los jugadores que participaron en el evento mundialista, sin distinción entre aquellos que fueron titulares o suplentes durante los partidos.

En lugar de seleccionar una muestra, se utilizaron los datos completos de todos los jugadores, los cuales se recogieron a través de observaciones detalladas de las grabaciones de los partidos y de los registros oficiales. En total, el conjunto de datos consta de 16 variables y 994 observaciones. Sin embargo, antes de llevar a cabo el análisis, se eliminaron 12 filas debido a la falta de información completa, incluyendo casos en los que el nombre del jugador no estaba disponible.

Posteriormente, se enfocó el análisis en cuatro variables importantes. La primera de ellas es la posición de los jugadores, una variable cualitativa nominal que engloba cuatro categorías que corresponden a los roles distintivos en el campo (portero, defensa, mediocentro y delantero). La segunda variable es la confederación, que designa la región geográfica a la que cada equipo pertenece. La tercera variable, los minutos jugados, es una variable cuantitativa de razón que registra una medición numérica precisa, con un punto cero absoluto, que representa cuando un jugador no ha participado en el juego; valores más altos indican un mayor tiempo de participación en el juego. La cuarta variable, los goles, también es una variable cuantitativa de razón; un gol se contabiliza cuando un jugador logra que el balón atraviese completamente la línea de gol y entre en la portería contraria; este es el indicador más crítico en el fútbol, dado que determina el ganador del partido.

Para las variables de posición y confederaciones, se crearon tablas de frecuencias y conteos, junto con gráficos de barras para facilitar la visualización de los datos. En cuanto a las variables cuantitativas, se calculó medidas como la mediana, desviación estándar, media aritmética, así como frecuencias absolutas, relativas e índices de correlación de Pearson. Adicionalmente, se crearon histogramas, diagramas de dispersión y gráficos de cajas y bigotes para representar estos datos de manera gráfica.
""",
                color_name="green-40")

builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_default_column(min_column_width= 5,
                                 resizable= True,
                                 filterable= True,
                                 sortable= True,
                                 editable= True,
                                 groupable= True)
builder.configure_auto_height(autoHeight= True)

builder.configure_side_bar(filters_panel = True,
                           columns_panel = True,
                           defaultToolPanel = 'Panel')

builder.configure_pagination(enabled=True,
                             paginationAutoPageSize=False,
                             paginationPageSize=20)
go = builder.build()

AgGrid(df,
       theme = "balham",
       columns_auto_size_mode= True,
       height= 100,
       gridOptions= go)

if st.button("Ir a Página Principal", key= "mi-boton"):
    switch_page("Principal")
