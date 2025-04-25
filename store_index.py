from src.helpers import load_pdf_file,text_split,download_hugging_face_embeddings
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import ServerlessSpec
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore

import os

PINECONEAPIKEY=os.getenv("PINECONE_API_KEY")

extracted_data=load_pdf_file(data='Data/')
text_chunks=text_split(extracted_data)
embeddings=download_hugging_face_embeddings()

from pinecone import ServerlessSpec
from pinecone import Pinecone
index_name="medical-rag-bot"


pc=Pinecone(api_key=PINECONE_API_KEY)

if not pc.has_index(name=index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric='dotproduct',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
index=pc.Index(name=index_name)

# Embed each chunk and upsert the embeddings into your Pinecone index.

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)

