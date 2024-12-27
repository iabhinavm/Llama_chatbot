import streamlit as st
from PIL import Image
from phi.agent import Agent
from phi.model.groq import Groq 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

# Load your custom image
bot_logo = Image.open('bot-logo.jpg') 
user_logo=Image.open('user_logo.jpg')
st.title("Llama Chatbot🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_response" not in st.session_state:
    st.session_state.current_response = ""


if prompt := st.chat_input("Enter your Query"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    data=agent.run(prompt)
    response=data.content
    st.session_state.messages.append({"role": "assistant", "content": response})
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message['role']=='user':
                st.image(user_logo,width=50)
            if message["role"] == "assistant":
                st.image(bot_logo, width=50) 
            st.markdown(message["content"])