import streamlit as st
import requests
import webbrowser
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed", page_title="Home")

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

st.title('Bem-Vindo(a) ao SweetChat')

show_pages(
    [
        Page("Home.py", "Home"),
        Page("pages/login.py", "Login"),
        Page("pages/signup.py", "Cadastro"),
        Page("pages/remedios.py", "Meus Medicamentos"),
        Page("pages/main.py", "Feed")
    ]
)

st.subheader('Não tem uma conta em nossa comunidade? Crie uma!')
if st.button('Cadastro'):
    switch_page("Cadastro")

st.subheader('Já tem uma conta em nossa comunidade? Faça o login!')
if st.button('Login'):
    switch_page("Login")
