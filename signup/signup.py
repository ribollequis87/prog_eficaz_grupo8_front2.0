import streamlit as st
import requests

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

# response = requests.get('http://10.102.5.181:8501/cadastro')
st.markdown('<h1 style="text-align:center;">Cadastro</h1>', unsafe_allow_html=True)
username = st.text_input("Insira seu username")
email = st.text_input("Insira seu e-mail")
password1 = st.text_input("Insira sua senha")
password2 = st.text_input("Confirme sua senha")
enviar = st.markdown("<div style='text-align: center;'><button>Enviar</button></div>", unsafe_allow_html=True)
# if enviar:
    # response = requests.get('http://10.102.5.181:8501/login')