from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate   
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv  
# load_dotenv(dotenv_path=".env", override=True)
# NOTE: For security, set your keys in a local .env (which is gitignored) or in environment variables.

model1=ChatOpenAI(
    model="gpt-4o-mini",    
    base_url="https://openrouter.ai/api/v1",    
    temperature=0.8
)
model2=ChatOpenAI(
    model="gpt-4o",    
    base_url="https://openrouter.ai/api/v1",    
    temperature=0.8
)   

prompt1=PromptTemplate(
    template='Generate short and simple notes on the following text: /n {text}',
    input_variables=['text']
)


prompt2=PromptTemplate(
    template='Generate 5  short question and answers on the following text: /n {text}', 
    input_variables=['text']
)


prompt3=PromptTemplate(
    template='Merge the following notes and Q&A into a comprehensive summary: /n Notes: {notes} /n Q&A: {q_and_a}', 
)

parser=StrOutputParser()
parallel_chain=RunnableParallel(
    {
        'notes': prompt1 | model1 | parser,
        'q_and_a': prompt2 | model2 | parser
    }
)
merge_chain= prompt3 | model1 | parser 
 
chain= parallel_chain | merge_chain
text='''Key Components of LLM Chains
LLMs (Large Language Models): The central generative model trained on extensive datasets to understand and generate human-like language.
Prompt Templates: Define how user inputs are formatted and structured to guide LLMs effectively. They enable modular prompt engineering for better control over responses.
Chains: Sequences of actions where each step involves querying an LLM, transforming data or interacting with external tools. These can be simple (single LLM call) or multi-step (several chained calls or actions).
Memory Management: Allows the LLM chain to retain context across interactions, useful for conversational agents requiring coherence over multiple turns.
Data Retrieval (Retrievers) and Vector Stores: External databases or vector stores enable retrieval-augmented generation (RAG). User queries are converted into vector embeddings, then matched with stored vectors to fetch relevant documents or information, improving factual accuracy and context relevance.
Agents: Autonomous components that decide dynamically which tasks to perform, may call APIs, query databases or split queries into subtasks. Agents add reasoning and decision capabilities to LLM chains.
Output Parsers and Postprocessors: Components that format, filter or enrich the LLM's raw output to fit the application's needs.
Error Handlers and Quality Controllers: Modules ensuring robustness by handling runtime errors, validating outputs and maintaining result quality.
Working of LLM Chain
Let's understand how LLM chains work,

User Query Input: The process begins when a user submits a query to the system.
Input Processing: Preprocessors clean and transform the user's input for compatibility with subsequent components.
Vector Embedding and Retrieval: The query is converted to a vector embedding, which is then used to search an external knowledge base or vector store for relevant context or documents.
Prompt Generation: The retrieved information and processed inputs are combined via prompt templates to formulate a context-rich prompt.
LLM Invocation: The language model generates a response based on the enriched prompt.
Postprocessing: The raw output is parsed and formatted, potentially checked for quality or further refined.
Response Delivery: The final, polished response is returned to the user.'''

result= chain.invoke({'text': text})    
print(result)
