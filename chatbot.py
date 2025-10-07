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
chat_history= []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print("Bot:", response.content) 

print(chat_history)
