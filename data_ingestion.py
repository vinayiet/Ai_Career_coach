from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile



def ingest_data(uploaded_file):
    
    if uploaded_file is not None:
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        # Load and process with PyPDFLoader
        loader = PyPDFLoader(tmp_file_path)
        documents = loader.load()
        return documents

# Data preparation 
def data_chunking(documents):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300, 
    chunk_overlap = 50,
    length_function = len,
    separators=['\n\n', '\n', " ", '']
    )

    chunks = text_splitter.split_documents(documents)
    return chunks
