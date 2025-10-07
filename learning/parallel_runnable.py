from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate   
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence
from dotenv import load_dotenv  
# load_dotenv(dotenv_path=".env", override=True)
model1=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    base_url="https://openrouter.ai/api/v1"
)
model2=ChatOpenAI(
    model="gpt-4o",     
    temperature=0.7,
    base_url="https://openrouter.ai/api/v1"
)   

prompt1=PromptTemplate(
    template='Generate a tweet on the following text: /n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate a LinkedIn post on the following text: /n {text}', 
    input_variables=['text']
)

parser=StrOutputParser()    
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model1, parser),
    'linkedin_post': RunnableSequence(prompt2, model2, parser)
})

result=parallel_chain.invoke({
    'text': 'Generative AI'
})

print(result)
