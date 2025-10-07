from langchain_community.document_loaders import PyPDFLoader    
from langchain_text_splitters import CharacterTextSplitter
splitter=CharacterTextSplitter(
    chunk_size=100,
    separator='',
    chunk_overlap=0
)
loader=PyPDFLoader(file_path='CV_new_.pdf')
doc=loader.load()
texts=splitter.split_documents(doc)
print(texts[0].page_content)
