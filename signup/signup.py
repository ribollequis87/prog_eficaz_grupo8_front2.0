import streamlit as st
import requests

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

def register_user(username, email, password):
    url_base = 'http://127.0.0.1:5000'  
    response = requests.post(f'{url_base}/cadastro', json={'username': username, 'email': email, 'password': password})
    return response

def cadastro():
    st.title('Cadastro')
    
    response = requests.get('http://10.102.5.181:8501/cadastro')
    username = st.text_input(label="Insira seu Username", value='', key='username')
    email = st.text_input("Insira seu e-mail")
    password = st.text_input(label="Insira sua senha", value='', key='senha', type='password')
    passoword2 = st.text_input(label="Confirme sua senha", value='', key='senha', type='password')
    # diabete = st.text_input(label="Insira seu Username", value='', key='username')
    if st.button('Cadastrar'):
        if username and email and password:
            if password == passoword2:
                st.session_state['username'] = username
                st.session_state['senha'] = password
                st.session_state['autenticado'] = True
                response = register_user(username, email, password)
                if response.status_code == 200:
                    st.success('Cadastro feito. Redirecionando para o login...')
            else:
                st.error(f'Erro no registro: {response.text}')
    
        else:
            st.warning('Por favor, preencha todos os campos.')

if st.button("Ir para a página de login"):
    st.session_state['pagina'] = 'login'
    st.rerun()
    st.rerun()

if __name__ == '__main__':
    cadastro()