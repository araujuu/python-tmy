import streamlit as st
import pandas as pd
import requests

url = "https://viacep.com.br/ws/{endereco}/json/"

st.title("Buscar CEP")

endereco = st.text_input("Busque seu cep: ")

if endereco != "":
    resp = requests.get(url.format(endereco=endereco))
    data = pd.DataFrame([resp.json()])
    st.dataframe(data)