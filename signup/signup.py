import streamlit as st
import requests

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

def register_user(username, email, password):
    url_base = 'http://127.0.0.1:5000'  
    response = requests.post(f'{url_base}/cadastro', json={'username': username, 'email': email, 'password': password})
    return response

def main():
    st.title('Cadastro')
    
    username = st.text_input('Nome de usuário')
    email = st.text_input('Email')
    password = st.text_input('Senha', type='password')

    if st.button('Cadastrar'):
        if username and email and password:
            response = register_user(username, email, password)
            if response.status_code == 200:
                st.success('Cadastro feito. Redirecionando para o login...')
            else:
                st.error(f'Erro no registro: {response.text}')
        else:
            st.warning('Por favor, preencha todos os campos.')

if __name__ == '__main__':
    main()