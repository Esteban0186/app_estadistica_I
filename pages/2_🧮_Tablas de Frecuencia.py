import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from Principal import df




colored_header(
                label="Tablas de Frecuencia",
                description="""Las variables cualitativas, como las posiciones en un equipo de fútbol, se pueden analizar mediante la generación de frecuencias simples, que cuentan cuántas veces aparece cada categoría en un conjunto de datos. En esta aplicación, los usuarios pueden seleccionar una variable, generar un resumen de frecuencias y visualizar la distribución en gráficos para un análisis eficiente.""",
                color_name="orange-40")


tab1, tab2 = st.tabs(["Frecuencias Simples", "Frecuencias cruzadas"])

with tab1:
     st.subheader("Tablas de frecuencias Simples")
     var_cual = selectbox("Seleccione una variable", ["País", "Región", "Posición"])

     if var_cual == None:
          st.warning("Para ver la tabla de frecuencias debe seleccionar una variable cualitativa")

     else:
          #Crear la tabla de frecuencias
          frecuencias = df[var_cual].value_counts()

          frecuencias_total = pd.DataFrame({var_cual: frecuencias.index, "Cantidad": frecuencias.values})
          total_general = {var_cual: "Total General", "Cantidad": frecuencias.sum()}

          frecuencias_total = pd.concat([frecuencias_total, pd.DataFrame(total_general, index=[0])], ignore_index=True)

          #frecuencias_total = frecuencias.append(pd.Series(frecuencias.sum(), index=["Total General"]))
          #frecuencias_total = frecuencias_total.reset_index().rename(columns={"index": var_cual, 0: "Cantidad"})

          #Quitar el índice

          ocultar_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
          st.markdown(ocultar_index, unsafe_allow_html=True)

          #Se utiliza una tabla estática

          st.table(frecuencias_total)



with tab2:
     st.subheader("Tabla de frecuencias cruzadas")

     var_cual1 = selectbox("Seleccione una primera variable", ["País", "Región", "Posición"])
     var_cual2 = selectbox("Seleccione una segunda variable", ["País","Región", "Posición"])

     if var_cual1 == var_cual2:
          st.warning("Elija dos variables diferentes")

     elif var_cual1 == None or var_cual2 == None:
          st.warning("Elija dos variables para obtener la tabla")

     elif var_cual2 == "País":
          tabla_cruzada = pd.crosstab(index=df[var_cual1], columns=df[var_cual2],
                                        margins=True, margins_name="Total General")

          tabla_cruzada = tabla_cruzada.transpose()
          tabla_cruzada = tabla_cruzada.reset_index()


          st.table(tabla_cruzada)

     else:
          tabla_cruzada = pd.crosstab(index=df[var_cual1], columns=df[var_cual2],
                                        margins=True, margins_name="Total General")

          tabla_cruzada = tabla_cruzada.reset_index()

          st.table(tabla_cruzada)

if st.button("Ir a Página Principal"):
    switch_page("Principal")

