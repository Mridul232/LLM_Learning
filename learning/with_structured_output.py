from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
from typing import TypedDict ,Annotated
# load_dotenv(dotenv_path=".env", override=True)
# Set your API key in .env or environment variables instead of hardcoding.

model=ChatOpenAI(
    model="gpt-4o-mini", 
    base_url="https://openrouter.ai/api/v1",    
    temperature=0.8
)
class review(TypedDict):
    summary:Annotated[str , "A brief summary of the review in one sentence."]
    sentiment:Annotated[str , "The sentiment of the review (e.g., positive, negative, neutral)."]


structured_model =  model.with_structured_output(review)

result=structured_model.invoke('Terrible customer service. I have contacted them 4 times about a damaged record I received and every time they just apologize and say they will contact the seller and get back to me. If I purchased the product on your website, you are the seller as far as I am concerned, which means you should be providing a resolution to the issues. I would steer clear of this company.')
print(result)
