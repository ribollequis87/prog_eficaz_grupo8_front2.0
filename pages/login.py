import streamlit as st
import requests
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page
from time import sleep

st.set_page_config(initial_sidebar_state="collapsed", page_title="Home - Login/Cadastro")

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

def login_user(username, password):
    url_base = 'http://127.0.0.1:5000'
    response = requests.post(f'{url_base}/login', json={'username': username, 'password': password})
    return response

def login():
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
                # redirecionar para a página inicial
                sleep(0.5)
                switch_page("Home")

                return response.json()
            else:
                st.error(f'Erro ao fazer o login: {response.text}')
        else:
            st.warning('Por favor, preencha todos os campos.')

if __name__ == '__main__':
    login()