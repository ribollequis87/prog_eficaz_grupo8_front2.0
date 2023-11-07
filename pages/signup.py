import streamlit as st
import json
import requests
import webbrowser
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page
from time import sleep

st.set_page_config(page_title="Cadastro", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }

    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""",
    unsafe_allow_html=True,
)

show_pages(
    [
        Page("Home.py", "Home"),
        Page("pages/login.py", "Login"),
        Page("pages/signup.py", "Cadastro"),
        Page("pages/remedios.py", "Meus Medicamentos"),
        Page("pages/main.py", "Feed")
    ]
)

def send_user_to_server(username, email, password):
    url_base = 'http://127.0.0.1:5000'
    
    response = requests.post(f'{url_base}/cadastro', json={'username': username, 'email': email, 'password': password})
    print(response.status_code)
    return response.status_code == 200

def cadastro():
    st.title('Cadastro')

    username = st.text_input('Nome de usuário')
    email = st.text_input('Email')
    password = st.text_input('Senha', type='password')

    if st.button('Cadastrar'):
        if username and email and password:
            if send_user_to_server(username, email, password):
                st.success('Cadastro feito. Redirecionando para o login...')
                # redirecionar para a página de login
                sleep(0.8)
                switch_page("Login")
            else:
                st.error(f'Erro no registro')
        else:
            st.warning('Por favor, preencha todos os campos.')

if __name__ == '__main__':
    cadastro()