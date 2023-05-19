import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from Principal import df
from st_aggrid import AgGrid
#pip install streamlit-aggrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

colored_header(
                label="Base de datos",
                description="Descripción",
                color_name="green-40")

st.dataframe(df.head(10))

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
                             paginationAutoPageSize=True,
                             paginationPageSize=100)
go = builder.build()

AgGrid(df.head(20),
       theme = "balham",
       columns_auto_size_mode= True,
       height= 100,
       gridOptions= go)

if st.button("Ir a Página Principal", key= "mi-boton"):
    switch_page("Principal")
