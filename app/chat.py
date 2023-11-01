import streamlit as st
import requests

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

# Tentativa de mudar o estilo do app
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

