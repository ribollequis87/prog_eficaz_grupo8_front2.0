import streamlit as st
import requests

def send_message_to_server(message):
    response = requests.post('http://127.0.0.1:5000/send_message', data={'message': message})
    print(response.status_code)
    return response.status_code == 201

# Create an input box for the user to type messages
message = st.text_input("Type your message:")

# Create a button to send the message to the server
if st.button("Send"):
    if message:
        if send_message_to_server(message):
            st.success("Message sent successfully") 
        else:
            st.error("Failed to send the message")
    else:
        st.warning("Please enter a message")

# You can also display the chat history or incoming messages here
# Use st.write or st.text to display the chat history

def get_messages_from_server():
    response = requests.get('http://127.0.0.1:5000/get_messages')
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Display messages
messages = get_messages_from_server()
for message in messages:
    st.write(message['message'])