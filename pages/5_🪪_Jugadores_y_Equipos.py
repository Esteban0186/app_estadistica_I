import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from Principal import df



colored_header(
    label="Estadísticas de jugadores y Equipos",
    description="""Buscar el nombre del jugador para ver sus estadísticas""",
                    color_name="green-40")

with st.expander("Jugadores"):
    nombre =st.text_input("Escribe el nombre del jugador")
    boton1 = st.button("Inciar búsqueda")

    if not boton1:
        st.warning("Escribe un nombre para hacer la búsqueda")

    else:
        resultado = df.loc[df["Jugador"].str.contains(nombre)]

        if nombre == "":
            st.warning("Escribe un nombre")

        elif len(resultado) == 0:
            st.warning("No se encontraron resutaldos")

        elif len(resultado) >= 2:
            st.warning("Hay varios nombres de jugadores que contienen ese texto, incluye tanto el apellido como el nombre para un mejor resultado")

        elif len(resultado) == 1:
            st.subheader(resultado["Jugador"].to_string(index = False))

            col1, col2, col3 = st.columns([1,2,2])

            with col1:
                    st.write("País: {}".format(resultado["País"].to_string(index=False)))
                    st.write("Región: {}".format(resultado["Región"].to_string(index=False)))
                    st.write("Posición: {}".format(resultado["Posición"].to_string(index=False)))

            with col2:

                    col2.metric(label="Edad", value= resultado["Edad"])
                    col2.metric(label="Partidos Jugados", value= resultado["Partidos Jugados"])
                    col2.metric(label="Partidos jugados desde el inicio", value= resultado["Partidos Inicial"])
                    col2.metric(label="Minutos Jugados", value= resultado["Minutos Jugados"])
                    col2.metric(label="Minutos jugados por partido", value= resultado["Minutos jugados por partido"])


            with col3:

                    col3.metric(label="Goles", value= resultado["Goles"])
                    col3.metric(label="Asistencias", value= resultado["Asistencias"])
                    col3.metric(label="Tarjetas Amarillas", value= resultado["Amarillas"])
                    col3.metric(label="Tarjetas Rojas", value= resultado["Rojas"])
                    col3.metric(label="Goles por minuto", value= resultado["Goles por minuto"])
                    col3.metric(label="Asistencias por minuto", value= resultado["Asistencias por minuto"])

with st.expander("Equipos"):
    st.subheader("Estadísticas de Equipos")
    pais =st.text_input("Escribe el nombre del país")
    boton2 = st.button("Inciar búsqueda ")

    if not boton2:
        st.warning("Escribe el nombre del país para hacer la búsqueda")

    else:
        resultado2 = df.loc[df["País"].str.contains(pais)]

        if pais == "":
            st.warning("Escribe el nombre de un páis")

        elif len(set(resultado2["País"])) >=2:
            st.warning("Hay varios países que coinciden con el texto, trata de escribir completamente el nombre")

        elif len(set(resultado2["País"])) == 1:
            st.dataframe(resultado2, use_container_width= True)

if st.button("Ir a Página Principal"):
    switch_page("Principal")