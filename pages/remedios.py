import streamlit as st
import requests
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed", page_title="Remédios")

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

if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'login'

if 'username' not in st.session_state:
    st.session_state['username'] = ''

if 'senha' not in st.session_state:
    st.session_state['senha'] = ''

if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

st.markdown('<h2 style="text-align:center;">Login</h2>', unsafe_allow_html=True)

def remedios():
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
    remedios()

