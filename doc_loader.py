from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
# load_dotenv(dotenv_path=".env", override=True)  

model=ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.8
)

parser=StrOutputParser()    

loader=PyPDFLoader(file_path='CV_new_.pdf')
doc=loader.load()   

# Create a prompt template that includes the document content
prompt = PromptTemplate(
    template="Based on the following document content, answer this question: {question}\n\nDocument Content:\n{content}",
    input_variables=["question", "content"]
)

chain = prompt | model | parser
result = chain.invoke({
    'question': 'what is this pdf about',
    'content': doc[0].page_content  # Extract the text content from the first page
})
# print(doc[0].page_content)  
print(result)
