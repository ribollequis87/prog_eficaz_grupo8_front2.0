import streamlit as st
import requests

if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'login'

if 'username' not in st.session_state:
    st.session_state['username'] = ''

if 'senha' not in st.session_state:
    st.session_state['senha'] = ''

if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

st.markdown('<h2 style="text-align:center;">Login</h2>', unsafe_allow_html=True)

def remedio():
    response = requests.get('http://10.102.5.181:8501/cadastro')
    remedio = st.text_input(label="Insira seu remédio", value='', key='remedio')
    frequencia = st.text_input(label="Insira sua frequência de uso", value='', key='frequencia')
    horario = st.time_input(label="Insira o horário")
    

    if st.button('Enviar'):
        if remedio and frequencia:  
            if response.status_code == 200:
                st.success('Cadastro feito. Redirecionando para o login...')
            else:
                st.error(f'Erro no registro: {response.text}')
        else:
            st.warning('Por favor, preencha todos os campos.')

if st.button("Adicionar remédio"):
    remedio()

