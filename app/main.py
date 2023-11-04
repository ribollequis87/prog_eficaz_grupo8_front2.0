import streamlit as st
import requests

url_base = 'http://127.0.0.1:5000'

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

menu = st.sidebar.selectbox('Menu', ['Home','Comunidade', 'Meus Medicamentos'])

# 1- Home

if menu == 'Home':
    # response = requests.get('http://10.102.5.181:8501/home')
    st.markdown('<h2 style="text-align:center;">Home</h2>', unsafe_allow_html=True)
    bem_vindos = f"Bem-vindo(a) à nossa comunidade!"
    st.markdown(f"<h3 style='text-align: center;'>{bem_vindos}</h3>", unsafe_allow_html=True)

# 2- Comunidade

if menu == 'Comunidade':
    url_base = 'http://127.0.0.1:5000'

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

        message_display = st.text_area("Mensagens", value="\n".join(message['message'] for message in messages), height=300, key="messages_display", disabled=True)

    st.markdown('<h2 style="text-align:center;">Comunidade</h2>', unsafe_allow_html=True)
    message = st.text_input("Digite sua mensagem:", key="message_input")

    def send_message_to_server(message):
        response = requests.post(f'{url_base}/send_message', data={'message': message})
        print(response.status_code)
        return response.status_code == 200

    # Botão para enviar a mensagem
    if st.button("Send"):
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

    with open('app/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
# 3- Meus Medicamentos        

if menu == 'Meus Medicamentos':
    st.markdown('<h2 style="text-align:center;">Meus Medicamentos</h2>', unsafe_allow_html=True)
    remedio = st.text_input("Adicione um novo Medicamento:")
    # response = requests.get('http://10.102.5.181:8501/avisos')              