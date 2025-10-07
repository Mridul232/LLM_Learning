from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load_dotenv(dotenv_path=".env", override=True)  
model=ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.8
)

prompt1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)


prompt2= PromptTemplate(
    template='Generate a 5 line summary of the following text: /n {text}',   
    input_variables=["text"]
)
parser=StrOutputParser()    
chain = prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({'topic': 'Unemployment in india'})
print(result)
chain.get_graph().print_ascii()
