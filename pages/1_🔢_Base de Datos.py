import streamlit as st
from streamlit_extras.colored_header import colored_header
from Principal import df


colored_header(
                label="Base de datos",
                description="Descripción",
                color_name="green-40")

st.dataframe(df.head(10))

st.markdown('<a href="/" target="Principal">Página Principal</a>', unsafe_allow_html=True)