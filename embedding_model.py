from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()


hf_token = os.getenv("HUGGING_TOKEN")
embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},  # Use 'cuda' if you have GPU
        encode_kwargs={'normalize_embeddings': True}  # Normalize for better similarity search
)

def embedding_text(chunks):
    texts = [chunk.page_content for chunk in chunks]
    embeded_text = embedding_model.embed_documents(texts)
    return embeded_text