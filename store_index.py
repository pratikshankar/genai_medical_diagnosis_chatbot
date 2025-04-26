from src.helper import load_pdf_file,text_split,download_hugging_face_embeddings
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import ServerlessSpec
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore

import os

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")

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
        dimension=768,
        metric='dotproduct',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
index=pc.Index(name=index_name)

# Embed each chunk and upsert the embeddings into your Pinecone index.

# docsearch = PineconeVectorStore.from_documents(
#     documents=text_chunks,
#     index_name=index_name,
#     embedding=embeddings, 
# )

documents = load_pdf_file('Data/')
text_chunks = text_split(documents)
embeddings = download_hugging_face_embeddings()
print("Proceeding with embeddings")

embedded_vectors = embeddings.embed_documents([chunk.page_content for chunk in text_chunks])
print("Embeddings generated")
# Prepare vectors for Pinecone
vectors = []
for i, (text_chunk, vector) in enumerate(zip(text_chunks, embedded_vectors)):
    vectors.append({
        "id": f"chunk-{i}",
        "values": vector,
        "metadata": {
            "text": text_chunk.page_content[:500],  # Keep metadata light!
            "source": text_chunk.metadata.get("source"),
            "page": text_chunk.metadata.get("page")
        }
    })
print("Vectors prepared for Pinecone")
# === Batch Upload Safely ===
def batch_upsert(index, vectors, batch_size=50):
    for i in range(0, len(vectors), batch_size):
        print(f"Uploading batch {i // batch_size + 1} of {len(vectors) // batch_size + 1}")
        batch = vectors[i:i+batch_size]
        index.upsert(vectors=batch)

batch_upsert(index, vectors, batch_size=40)  # 40 is a safe number for 768 dim
print("✅ All chunks uploaded safely without exceeding Pinecone size limits.")
