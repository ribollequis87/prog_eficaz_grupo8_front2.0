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

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

if st.button("Ir para a página de cadastro"):
    st.session_state['pagina'] = 'cadastro'
    st.rerun()
    st.rerun()

def login_user(username, password):
    url_base = 'http://127.0.0.1:5000'
    response = requests.post(f'{url_base}/login', json={'username': username, 'password': password})
    return response

def liberou(username, password):
    # nao sei como conectar com o banco de dados no back, fiz só com o cadastro obrigatório
    if st.session_state['username'] == username and st.session_state['senha'] == password:
        st.session_state['autenticado'] = True
    else:
        st.session_state['autenticado'] = False
        st.error('Senha ou usuário inválido')

def main():
    url_base = 'http://127.0.0.1:5000'
    response = requests.get(f'{url_base}/home')

    st.title('Login')

    if 'autenticado' not in st.session_state:
        username = st.text_input(label="Insira seu Username", value='', key='username', on_change=liberou(username, password))
        password = st.text_input(label="Insira sua senha", value='', key='senha', type='password', on_change=liberou(username, password))

    else:
        if not st.session_state['autenticado']:
            username = st.text_input(label="Insira seu Username", value='', key='username', on_change=liberou(username, password))
            password = st.text_input(label="Insira sua senha", value='', key='senha', type='password', on_change=liberou(username, password))

    if st.button('Login'):
        if username and password:
            response = login_user(username, password)
            if response.status_code == 200:
                st.success('Login bem-sucedido. Redirecionando para a página inicial...')
                return response.json()
            else:
                st.error(f'Erro ao fazer o login: {response.text}')
        else:
            st.warning('Por favor, preencha todos os campos.')

if __name__ == '__main__':
    main()

