
import streamlit as st
import pandas as pd


nome = "Eduardo Aquino"  
idade = 18            

st.write(" Olá, meu nome é", nome, "e eu tenho", idade, "anos")

df = pd.DataFrame({
    'Matéria': ['Português', 'Matemática', 'Python', 'Frame'],
    'Nota': [6, 7, 10, 10]
})


st.title("Meu primeiro dash")

st.subheader(nome)

st.write(df)
