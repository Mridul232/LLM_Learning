from langchain_openai import ChatOpenAI  
from dotenv import load_dotenv
import os

# load_dotenv(dotenv_path=".env", override=True)
# api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1.5,
    base_url="https://openrouter.ai/api/v1",
)

result = model.invoke("write a 4 line poem about a lonely computer")
print(result.content)
