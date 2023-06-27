import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from Principal import df
from st_aggrid import AgGrid
#pip install streamlit-aggrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

colored_header(
                label="Metodología y Base de datos",
                description="""ste estudio analiza el rendimiento de los jugadores en la Copa Mundial de Qatar 2022, utilizando el software R para realizar el análisis estadístico. Los datos provienen del sitio web oficial de la FIFA e incluyen a todos los jugadores participantes. Se analizaron cuatro variables principales: posición del jugador, confederación, minutos jugados y goles. Se generaron tablas de frecuencias, gráficos de barras y otras medidas estadísticas para las variables. Además, se utilizaron gráficos como histogramas, diagramas de dispersión y gráficos de cajas para visualizar los datos.
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
