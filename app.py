import streamlit as st
from data_ingestion import ingest_data, data_chunking
from vector_db import vector_database
from embedding_model import embedding_model
from answer_generation import generate_answer

st.set_page_config(page_title="AI Career Coach 🤖💼", layout="wide")

# Sidebar
with st.sidebar:
    st.title("👋 Welcome to AI Career Coach")
    st.markdown("""
    - Upload your **resume PDF**
    - Ask questions like:
        - _"What skills am I missing for ML Engineer?"_
        - _"Suggest a roadmap to become a Data Scientist."_
    - Get personalized **learning plans**, **resources**, and **interview tips**.
    """)

# Header
st.title("🚀 Your Personalized AI Career Coach")
st.subheader("Upload your resume and let the coach help you grow!")

# ✅ Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vectordb" not in st.session_state:
    st.session_state.vectordb = None

if "full_resume_text" not in st.session_state:
    st.session_state.full_resume_text = ""

# Upload section
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("🔍 Analyzing your resume and building your personalized vector database..."):
        if st.session_state.vectordb is None:
            documents = ingest_data(uploaded_file)
            chunks = data_chunking(documents)

            # ✅ Save vector DB and full text to session state
            vectordb = vector_database(chunks)
            st.session_state.vectordb = vectordb
            st.session_state.full_resume_text = " ".join([doc.page_content for doc in documents])

    # Chat section
    st.markdown("### 💬 Ask Anything About Your Career")
    user_input = st.chat_input("What would you like to know? (e.g., 'Give me a roadmap for ML Engineer')")

    if user_input:
        resume_text = st.session_state.full_resume_text
        answer = generate_answer(resume_text, user_input)

        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("assistant", answer))

    # Display chat messages in style
    for speaker, message in st.session_state.chat_history:
        if speaker == "user":
            with st.chat_message("user"):
                st.markdown(f"👤 **You**: {message}")
        else:
            with st.chat_message("assistant"):
                st.markdown(f"🤖 **Coach**: {message}")

    # Future roadmap visualization section
    st.divider()
    st.markdown("📈 *Soon: Visual roadmap will be displayed here!*")

else:
    st.info("📎 Please upload your resume to begin.", icon="ℹ️")
