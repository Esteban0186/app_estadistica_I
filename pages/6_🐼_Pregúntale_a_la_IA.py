from Principal import df
import streamlit as st
from streamlit_extras import colored_header
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI


def chatea_con_df(prompt):
    llm = OpenAI(api_token= st.secrets["open_api"])
    pandas_ai = PandasAI(llm)
    resultado = pandas_ai.run(df, prompt = prompt)
    print(resultado)
    return resultado

colored_header(
    label="EPregúntale a la IA",
    description="""Aquí puedes utilizar chat GPT para hacer tus preguntas a los datos""",
                    color_name="green-40")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Base de datos")
    st.dataframe(df, use_container_width= True)

with col2:
    st.info("Chatea con Chat GPT")
    texto = st.text_area("Ingresa tu consulta")
    if texto is not None:
        if st.button("Consultar"):
            st.info("Tu consulta: " + texto)
            resultados = chatea_con_df(texto)
            st.success(resultados)


