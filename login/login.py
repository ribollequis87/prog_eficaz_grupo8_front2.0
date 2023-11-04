import streamlit as st
import requests

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

def login_user(username, password):
    url_base = 'http://127.0.0.1:5000'
    response = requests.post(f'{url_base}/login', json={'username': username, 'password': password})
    return response

def main():
    url_base = 'http://127.0.0.1:5000'
    response = requests.get(f'{url_base}/home')

    st.title('Login')
    
    username = st.text_input('Nome de usuário')
    password = st.text_input('Senha', type='password')


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