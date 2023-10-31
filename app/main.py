import streamlit as st
import requests

st.set_page_config(page_title="Projeto", layout="wide", initial_sidebar_state="expanded")

menu = st.sidebar.selectbox('Menu', ['Home', 'Comunidades', 'Avisos'])

if menu == 'Home':
    # response = requests.get('http://10.102.5.181:8501/home')
    st.markdown('<h2 style="text-align:center;">Home</h2>', unsafe_allow_html=True)
    usuario = "username"
    bem_vindos = f"Bem-vindo(a) à nossa comunidade {usuario}!"
    st.markdown(f"<h3 style='text-align: center;'>{bem_vindos}</h3>", unsafe_allow_html=True)

if menu == 'Comunidades':
    # response = requests.get('http://10.102.5.181:8501/communities')
    st.header('**Comunidades**')
    room = st.text_input("Escontre uma Nova Comunidade")
    st.button("Procurar")
    st.markdown("## Minhas Comunidades")

if menu == 'Avisos':
    st.markdown('<h1 style="text-align:center;">Avisos</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    # response = requests.get('http://10.102.5.181:8501/avisos')

    with col1:
        st.markdown('<h2 style="text-align:center;">Notificações</h2>', unsafe_allow_html=True)
        st.write("Notificação 1: @ acabou de aceitar seu pedido de amizade.")
        st.write("Notificação 2: hora do medicamento x.")
        st.write("Notificação 3: @ está tentando te mandar mensagem.")

    with col2:
        st.markdown('<h2 style="text-align:center;">Medicamentos</h2>', unsafe_allow_html=True)
        st.write("Medicamento x.")
        st.write("Medicamento y.")
        st.write("Medicamento z.")
              