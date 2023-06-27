import streamlit as st
from streamlit_extras.colored_header import colored_header
from Principal import df
import statistics
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.switch_page_button import switch_page
import numpy as np



colored_header(
            label="Descriptivos",
            description="""La aplicación permite calcular y visualizar estadísticas descriptivas clave como la media, moda, mediana y desviación estándar. Por ejemplo, en un equipo de fútbol, se podría determinar la posición más común (moda) o calcular estas estadísticas para variables cuantitativas como la edad o los goles marcados.""",
            color_name="blue-40")

tab1, tab2 = st.tabs(["Medidas de tendencia central", "Medidas de dispersión"])

with tab1:
    st.subheader("Medidas de tendencia cental")
    st.write("Descripción de lo que es una media, moda, y mediana")

    var_num = selectbox("Seleccione una variable de la lista",
                            ["Edad", "Partidos Jugados", "Partidos Inicial",
                                "Minutos Jugados", "Goles", "Asistencias", "Amarillas",
                                "Rojas","Minutos jugados por partido", "Goles por minuto", "Asistencias por minuto"])
    if var_num == None:
        st.warning("Seleccione una variable")

    else:

        #Medidas de tendencia central

        media = round(statistics.mean(df[var_num]), 2)
        mediana = statistics.median(df[var_num])
        moda  = statistics.mode(df[var_num])


        #Métricas
        col1, col2, col3 = st.columns(3)


        col1.metric(label="Media", value= media)
        col2.metric(label="Mediana", value= mediana)
        col3.metric(label="Moda", value= moda)


        #Agrupadas por variables

        st.subheader("Agrupadas por variables")
        st.write("Descripción de lo que se puede hacer")

        #Seleccione una variable

        st.write("Se pide seleccionar una variable")

    with st.expander("Región"):
        st.write("Las estadísticas muestran la media, mediana y moda de los jugadores en la región en cada variable")
        var_num = st.selectbox("Variable", ["Edad", "Partidos Jugados", "Partidos Inicial",
                                                            "Minutos Jugados", "Goles", "Asistencias", "Amarillas",
                                                            "Rojas","Minutos jugados por partido", "Goles por minuto", "Asistencias por minuto"])
        var_region = st.selectbox("", ["CONCACAF","CONMEBOL","UEFA","CAF","AFC"])


        media_r = round(df.loc[df["Región"] == var_region,var_num].mean(), 2)
        mediana_r = df.loc[df["Región"] == var_region,var_num].median()
        moda_r = df.loc[df["Región"] == var_region,var_num].mode()[0]
        cantidad_r = len(df.loc[df["Región"] == var_region,var_num])

        #Región Métricas
        col1, col2, col3, col4 = st.columns(4)


        col1.metric(label="Media", value= media_r)
        col2.metric(label="Mediana", value= mediana_r)
        col3.metric(label="Moda", value= moda_r)
        col4.metric(label= "Cantidad de Jugadores", value = cantidad_r)

    with st.expander("País y posiciones"):
        st.write("Se muestran la media, mediana y moda por cada posición y país")
        var_num = st.selectbox("Variable ", ["Edad", "Partidos Jugados", "Partidos Inicial",
                                                            "Minutos Jugados", "Goles", "Asistencias", "Amarillas",
                                                            "Rojas","Minutos jugados por partido", "Goles por minuto", "Asistencias por minuto"])
        var_pais = st.selectbox("País", ["Costa Rica","Ecuador","Netherlands","Senegal","England","IR Iran","United States",
                                                        "Wales","Argentina","Mexico","Poland","Australia","Denmark",
                                                        "France","Tunisia","Germany","Japan","Spain",
                                                        "Belgium","Canada","Croatia","Morocco","Brazil","Cameroon",
                                                        "Serbia","Switzerland","Ghana","Korea Republic","Portugal","Uruguay"])
        var_posicion = st.selectbox("Posición", ["Defensa","Mediocentro","Delantero","Portero"])



        df_pp = df.loc[(df['País'] == var_pais) & (df['Posición'] == var_posicion)]
        media_pp = round(df_pp[var_num].mean(), 2)
        mediana_pp = df_pp[var_num].median()
        moda_pp = df_pp[var_num].mode()[0]
        cantidad_pp = len(df_pp)

    #País posición Métricas
        col1, col2, col3, col4 = st.columns(4)


        col1.metric(label="Media", value= media_pp)
        col2.metric(label="Mediana", value= mediana_pp)
        col3.metric(label="Moda", value= moda_pp)
        col4.metric(label= "Cantidad de Jugadores", value = cantidad_pp)





with tab2:
    st.subheader("Medidas de dispersión")
    st.write("Descripción de lo que es la varianza, la desviación estándar y el rango intercuartil")

    var_num2 = selectbox("Seleccionar una variable de la lista",
                            ["Edad", "Partidos Jugados", "Partidos Inicial",
                                "Minutos Jugados", "Goles", "Asistencias", "Amarillas",
                                "Rojas","Minutos jugados por partido", "Goles por minuto", "Asistencias por minuto"])

    #Medidas de dispersión

    if var_num2 == None:
        st.warning("Elija una variable")

    else:
        ds = round(np.std(df[var_num2]), 2)
        var = round(np.var(df[var_num2]), 2)
        ric = round(np.subtract(*np.percentile(df[var_num2], [75, 25])), 2)


        #Métricas
        col1, col2, col3 = st.columns(3)

        col1.metric(label="Desviación Estándar", value= ds)
        col2.metric(label="Varianza", value= var)
        col3.metric(label="Rango intercuartil", value= ric)

        #Agrupadas por variables

        st.subheader("Agrupadas por variables")
        st.write("Descripción de lo que se puede hacer")

        #Seleccione una variable

        st.write("Se pide seleccionar una variable")

    with st.expander("Región"):
        st.write("Las estadísticas muestran la desviación estándar, varianza y rango intercuartil de los jugadores en la región en cada variable")
        var_num = st.selectbox("Variable   ", ["Edad", "Partidos Jugados", "Partidos Inicial",
                                                            "Minutos Jugados", "Goles", "Asistencias", "Amarillas",
                                                            "Rojas","Minutos jugados por partido", "Goles por minuto", "Asistencias por minuto"])
        var_region = st.selectbox("Región ", ["CONCACAF","CONMEBOL","UEFA","CAF","AFC"])


        ds_r = round(df.loc[df["Región"] == var_region,var_num].std(), 2)
        var_r = round(df.loc[df["Región"] == var_region,var_num].var(),2)
        ric_r = round(np.subtract(*np.percentile(df[var_num], [75, 25])), 2)
        cantidad_r = len(df.loc[df["Región"] == var_region,var_num])

        #Región Métricas
        col1, col2, col3, col4 = st.columns(4)


        col1.metric(label="Desviación estándar", value= ds_r)
        col2.metric(label="Varianza", value= var_r)
        col3.metric(label="Rango intercuartil", value= ric_r)
        col4.metric(label = "Cantidad de Jugadores", value = cantidad_r)

    with st.expander("País y posiciones"):
        st.write("Se muestran la desviación estándar, varianza y rango intercuartil por cada posición y país")
        var_num = st.selectbox("Variable  ", ["Edad", "Partidos Jugados", "Partidos Inicial",
                                                            "Minutos Jugados", "Goles", "Asistencias", "Amarillas",
                                                            "Rojas","Minutos jugados por partido", "Goles por minuto", "Asistencias por minuto"])
        var_pais = st.selectbox("País ", ["Costa Rica","Ecuador","Netherlands","Senegal","England","IR Iran","United States",
                                                        "Wales","Argentina","Mexico","Poland","Australia","Denmark",
                                                        "France","Tunisia","Germany","Japan","Spain",
                                                        "Belgium","Canada","Croatia","Morocco","Brazil","Cameroon",
                                                        "Serbia","Switzerland","Ghana","Korea Republic","Portugal","Uruguay"])
        var_posicion = st.selectbox("Posición ", ["Defensa","Mediocentro","Delantero","Portero"])



        df_pp = df.loc[(df['País'] == var_pais) & (df['Posición'] == var_posicion)]
        ds_pp = round(df_pp[var_num].std(), 2)
        var_pp = round(df_pp[var_num].var(),2)
        ric_pp = round(np.subtract(*np.percentile(df_pp[var_num], [75, 25])), 2)
        cantidad_pp = len(df_pp)

        #País posición Métricas
        col1, col2, col3, col4 = st.columns(4)


        col1.metric(label="Desviación Estándar", value= ds_pp)
        col2.metric(label="Varianza", value= var_pp)
        col3.metric(label="Rango Intercuartil", value= ric_pp)
        col4.metric(label="Cantidad de Jugadores", value= cantidad_pp)

if st.button("Ir a Página Principal"):
    switch_page("Principal")
