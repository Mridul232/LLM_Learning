from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
import os

# load_dotenv(dotenv_path=".env", override=True)  
# api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1",
    temperature=1.5
)

# Example Streamlit UI code
try:
    import streamlit as st
    st.header("Chat with GPT")
    user_input = st.text_input("Enter your prompt")
    if st.button('submit'):
        result = model.invoke(user_input)   
        st.write(result.content)
except Exception:
    pass
