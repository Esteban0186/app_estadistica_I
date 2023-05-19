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
builder.configure_column("first_column", header_name="First", editable=True)
go = builder.build()

AgGrid(df,
       theme = "balham",
       columns_auto_size_mode= True,
       gridOptions= go)

if st.button("Ir a Página Principal", key= "mi-boton"):
    switch_page("Principal")
