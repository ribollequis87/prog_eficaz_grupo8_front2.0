import streamlit as st
import requests
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Feed", layout="wide", initial_sidebar_state="expanded")

show_pages(
    [
        Page("Home.py", "Home"),
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

url_base = 'https://sweetchat-dd71ea0a10a1.herokuapp.com'


menu = st.sidebar.selectbox('Menu', ['Home','Comunidade', 'Meus Medicamentos'])

# botão de logout que siwtch para page de login
if st.sidebar.button('Logout'):
    switch_page('Home')


# 1- Home

if menu == 'Home':
    st.markdown('<h2 style="text-align:center;">Home</h2>', unsafe_allow_html=True)
    bem_vindos = f"Bem-vindo(a) à comunidade SweetChat!"
    st.markdown(f"<h3 style='text-align: center;'>{bem_vindos}</h3>", unsafe_allow_html=True)

# 2- Comunidade

if menu == 'Comunidade':
    url_base = 'https://sweetchat-dd71ea0a10a1.herokuapp.com'

    def get_messages_from_server():
        response = requests.get(f'{url_base}/get_messages')
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error response: {response.status_code}, {response.text}")
            return []

    # Mostra as mensagens do servidor
    def display_messages():
        messages = get_messages_from_server()
        messages = messages[::-1]
        messages.reverse()

        message_display = st.text_area("Mensagens", value="\n".join(f"{message['message']} - {message['datetime']}" for message in messages), height=300, key="messages_display", disabled=True)

    st.markdown('<h2 style="text-align:center;">Comunidade</h2>', unsafe_allow_html=True)
    message = st.text_input("Digite sua mensagem:", key="message_input")

    def send_message_to_server(message):
        response = requests.post(f'{url_base}/send_message', data={'message': message})
        print(response.status_code)
        return response.status_code == 200

    # Botão para enviar a mensagem
    if st.button("Enviar"):
        if message:
            if send_message_to_server(message):
                st.success("Mensagem enviada com sucesso")
                # Limpa o campo de mensagem
                message = ""
            else:
                st.error("Falha ao enviar mensagem")
        else:
            st.warning("Por favor, digite sua mensagem")

    display_messages()
        
# 3- Meus Medicamentos        

if menu == 'Meus Medicamentos':
    remedios = []
    st.markdown('<h2 style="text-align:center;">Meus Medicamentos</h2>', unsafe_allow_html=True)
    remedio = st.text_input("Adicione um novo Medicamento:")
    if st.button('Adicionar'):
        st.session_state.user_entries.append(remedio)  

    if 'user_entries' not in st.session_state:
        st.session_state.user_entries = []

    st.write('Medicamentos registrados:')
    for entry in st.session_state.user_entries:
        st.write(entry)