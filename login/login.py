import streamlit as st
import requests

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

# response = requests.get('http://10.102.5.181:8501/login')
st.markdown('<h2 style="text-align:center;">Login</h2>', unsafe_allow_html=True)
username = st.text_input("Insira seu Username")
password = st.text_input("Insira sua senha")
enviar = st.button("Enviar")
# if enviar:
    # response = requests.get('http://10.102.5.181:8501/home')