import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from Principal import df




colored_header(
                label="Tablas de Frecuencia",
                description="""En nuestra aplicación, proporcionamos funcionalidades que permiten la generación de frecuencias simples a partir de variables cualitativas. Este proceso es esencial para el análisis estadístico y la interpretación de datos.

Las variables cualitativas, también conocidas como variables categóricas, representan características o atributos que pueden clasificarse en distintas categorías pero que no pueden medirse en términos cuantitativos. Ejemplos de estas variables incluyen las posiciones en un equipo de fútbol: delantero, defensa, portero y mediocentro.

La generación de frecuencias simples consiste en contar la cantidad de veces que cada categoría de una variable cualitativa aparece en el conjunto de datos. Estas frecuencias proporcionan una descripción resumida y comprensible del patrón de los datos.

Por ejemplo, si tenemos una variable cualitativa "Posición en el equipo" con las categorías "Delantero", "Defensa", "Portero" y "Mediocentro", la generación de frecuencias simples consistiría en contar cuántas veces aparece cada una de estas posiciones en nuestro conjunto de datos.

En nuestra aplicación, el usuario puede seleccionar fácilmente la variable cualitativa de interés y generar un resumen de frecuencias simples con un solo clic. Además, se puede visualizar la distribución de las frecuencias en gráficos de barras o pastel para una interpretación visual más intuitiva.

Esta funcionalidad resulta ser muy útil para una amplia gama de aplicaciones, incluyendo el análisis deportivo, la investigación de rendimiento de equipos, la estrategia de juego y mucho más, permitiendo a los usuarios explorar y entender sus datos de manera más eficiente.""",
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

