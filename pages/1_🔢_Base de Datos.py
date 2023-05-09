import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page


from Principal import df


colored_header(
                label="Base de datos",
                description="Descripción",
                color_name="green-40")

st.dataframe(df.head(10))

if st.button("Ir a Página Principal"):
    switch_page("Principal")

