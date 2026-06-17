import streamlit as st
from dotenv import load_dotenv

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vectorstore
from utils.rag_chain import get_llm, build_prompt

load_dotenv()

# PAGE CONFIG  
st.set_page_config(
    page_title="AI PDF Chatbot",
    layout="centered"
)

# SESSION STATE 
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# LANDING UI 
uploaded_file = None

if st.session_state.vectorstore is None:

    st.markdown(
        """
        <div style="text-align:center; padding:30px 10px;">
            <h1 style="color:#2E86C1;">  AI PDF Chatbot</h1>
            <p style="color:gray; font-size:16px;">
                Upload your PDF and ask questions using AI-powered search
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("###   Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="padding:15px; border-radius:12px; background:#f5f7fa; text-align:center;">
        📄<br><b>PDF Reader</b><br>
        Extract text from documents
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="padding:15px; border-radius:12px; background:#f5f7fa; text-align:center;">
        🔍<br><b>AI Search</b><br>
        Understand context automatically
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="padding:15px; border-radius:12px; background:#f5f7fa; text-align:center;">
        💬<br><b>Instant Answers</b><br>
        Chat with your document
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

# UPLOAD 
uploaded_file = st.file_uploader("📁 Upload your PDF to begin", type="pdf")

#PROCESS PDF 
if uploaded_file:

    if st.button("Process PDF"):

        text = load_pdf(uploaded_file)
        chunks = split_text(text)

        st.success(f"Extracted {len(chunks)} chunks from PDF")

        embeddings = get_embeddings()
        vectorstore = create_vectorstore(chunks, embeddings)

        st.session_state.vectorstore = vectorstore

        st.success("Vector DB ready! Start chatting below")

# CHAT 
if st.session_state.vectorstore:

    st.markdown("## Chat with your PDF")

    query = st.chat_input("Ask anything from your document...")

    llm = get_llm()

    if query:

        st.session_state.messages.append({
            "role": "user",
            "content": query
        })

        docs = st.session_state.vectorstore.similarity_search(query, k=5)

        if not docs:
            answer = "No relevant information found in the document."
        else:
            context = "\n\n".join([d.page_content for d in docs])

            prompt = build_prompt(context, query)
            response = llm.invoke(prompt)
            answer = response.content

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

# CHAT UI (BUBBLES) 
for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                color: white;
                padding: 10px 15px;
                border-radius: 15px;
                margin: 8px 0;
                max-width: 75%;
                margin-left: auto;
                box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
            ">
                {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background: #f1f3f5;
                color: #222;
                padding: 10px 15px;
                border-radius: 15px;
                margin: 8px 0;
                max-width: 75%;
                box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
            ">
                {msg["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )