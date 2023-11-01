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

# Display the chat history or incoming messages
# Fetch and display messages
def display_messages():
    messages = get_messages_from_server()

    # Reverse the order of messages so that new messages appear at the bottom
    messages = messages[::-1]
    messages.reverse()

    # Create a text area to display messages
    message_display = st.text_area("Mensagens", value="\n".join(message['message'] for message in messages), height=300, key="messages_display", disabled=True)

# Create an input box for the user to type messages
message = st.text_input("Digite sua mensagem:")

def send_message_to_server(message):
    response = requests.post(f'{url_base}/send_message', data={'message': message})
    print(response.status_code)
    return response.status_code == 200

# Create a button to send the message to the server
if st.button("Send"):
    if message:
        if send_message_to_server(message):
            st.success("Mensagem enviada com sucesso")
            # Clear the input box after sending the message
            message = ""
        else:
            st.error("Falha ao enviar mensagem")
    else:
        st.warning("Por favor, digite sua mensagem")

display_messages()
