import streamlit as st
from streamlit_extras.colored_header import colored_header
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.no_default_selectbox import selectbox
import pandas as pd
import numpy as np
from Principal import df


colored_header(
    label="Gráficos",
    description="Descripción",
    color_name="yellow-40")

tab1, tab2, tab3 = st.tabs(["Variables Cualitativas", "Variables Discretas", "Variables Continuas"])

with tab1:
        st.subheader("Variables Cualitativas")
        st.write("Descripción del tipo de variable y de gráficos")

        var_cual = selectbox("Elija una variable para el gráfico", ["País", "Región", "Posición"])

        if var_cual == None:
               st.warning("Seleccione una variable para obtener el gráfico")
        else:
               
               conteos = pd.DataFrame(df[var_cual].value_counts())
               conteos = conteos.reset_index()
               conteos = conteos.rename(columns={var_cual: 'Cantidad', 'index': var_cual})
               fig1 = px.bar(conteos, x=conteos.index, y= var_cual)#, 
                            #orientation= "h",
                            #title= "Cantidad de jugadores por la variable {}".format(var_cual),
                            #labels={"Cantidad": "Cantidad de jugadores", var_cual: str(var_cual)},
                            #text= "Cantidad",height=400)
                

            
               st.plotly_chart(fig1, use_container_width= True)

with tab2:
       st.subheader("Variables Continuas")
       st.write("Descripción del tipo de variable y gráfico")

       var_disc = selectbox("Elija una variable para el gráfico", ["Edad", "Partidos Jugados", "Partidos Inicial",
                                                            "Minutos Jugados", "Goles", "Asistencias", "Amarillas", "Rojas"])
       if var_disc == None:
            st.warning("Elija una variable para obtener el gráfico")
       else:
            fig2 = go.Figure()
            fig2.add_trace(go.Histogram(x=df[var_disc]))

            fig2.update_layout(
                        title_text='Histograma de la variable {}'.format(var_disc), # title of plot
                        xaxis_title_text='Valor',
                        yaxis_title_text='Cantidad')

            st.plotly_chart(fig2, use_container_width= True)

with tab3:
       st.subheader("Variables Discretas")
       st.write("Descripción de las variables y el gráfico")
       var_cont = selectbox("Elija una variable para obtener el gráfico", ["Minutos jugados por partido",
                                                                    "Goles por minuto", "Asistencias por minuto"])

       if var_cont == None:
            st.warning("Elija una variable para obtener el gráfico")
       
       else:
            fig1 = px.violin(df, x= var_cont, box=True, points="all")
            fig1.update_layout(title="Gráfico de violín de {}".format(var_cont), xaxis_title= var_cont)
            st.plotly_chart(fig1, use_container_width= True)

       st.subheader("Variables agrupadas por Posición")

       with st.expander("Posiciones"):
        st.write("Se muestran las posiciones y las agrupaciones por cada variable")
        var_cont = st.selectbox("Elija una variable para obtener el gráfico ", ["Minutos jugados por partido",
                                                                    "Goles por minuto", "Asistencias por minuto"])

        fig3 = px.violin(df, x= var_cont, box=True, points="all", color='Posición', height= 900)
        fig3.update_layout(title="Gráfico de violín de {} agrupados por posición".format(var_cont), xaxis_title= var_cont)
        st.plotly_chart(fig3, use_container_width= True)
