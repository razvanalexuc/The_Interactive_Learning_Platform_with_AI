import streamlit as st
from streamlit.components.v1 import html
from dotenv import load_dotenv
from langchain.embeddings import openai
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS # necesita instalata si libraria FAISS CPU pentru a rula embedding-ul pe cpu 
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from streamlit_login_auth_ui.widgets import __login__
from templates.template_html import css, bot_template, user_template, flashcard_template, flashcard_script
from templates.streamlit_components import flashcard_component
from handlers.userinput import handle_userinput
from authentication.auth import check_login
from utils.inputs import get_pdf_text, get_text_chunks
from flashcards.cards import generate_flashcards, display_flashcard
from constants import HUGGINGFACEHUB_API_TOKEN

def get_vectorstore_openai(text_chunks):
    embeddings = openai()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_vectorstore_huggingface(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 1, "max_length": 512},
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        return_messages=True,
    )
    retriever = vectorstore.as_retriever()
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=retriever, 
        memory=memory,
        chain_type="stuff",
    ) 
    return conversation_chain, llm

def main():
    login_status = check_login()
    if login_status:
        st.title("Platformă de învățare interactivă cu flashcard-uri și interacțiune conversațională 📄")
        st.markdown(css, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Acordă întrebări", "Generează Flashcard"])

        if "conversation" not in st.session_state:
            st.session_state.conversation = None

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None

        with st.sidebar:
            st.subheader("Documente: ")
            pdf_docs = st.file_uploader("Incarca fisierul PDF si apasa pe 'Procesare'", accept_multiple_files=True)

            if st.button("Procesare"):
                if pdf_docs:
                    with st.spinner("Proceseaza..."):
                        raw_text = get_pdf_text(pdf_docs)
                        st.write("Textul PDF a fost extras cu succes.")
                        text_chunks = get_text_chunks(raw_text)
                        st.write("Chunk-urile au fost create cu succes.")
                        vectorstore = get_vectorstore_huggingface(text_chunks)
                        st.write("Vectorstore creat cu succes.")
                        conversation_chain, llm = get_conversation_chain(vectorstore)
                        st.session_state.conversation = conversation_chain
                        st.session_state.vectorstore = vectorstore
                        st.session_state.text_chunks = text_chunks
                        st.session_state.llm = llm
                        st.write("LLM initializat si stocat cu succes.")
                        st.experimental_rerun()
                else:
                    st.warning("Te rog incarca un PDF.")
            else:
                if "vectorstore" in st.session_state:
                    st.warning("Pentru a genera noi flashcard-uri, reincarca si reproceseaza documentul PDF.")

        with tab1:
            st.header("Conversează! :books:")
            if "vectorstore" in st.session_state:
                user_question = st.text_input("Pune o întrebare despre documentul atașat:")
                if user_question:
                    handle_userinput(user_question)
            else:
                st.warning("Te rog incarca un PDF.")

        with tab2:
            st.header("Meniul de generare pentru carduri flash! 🀫")
            flashcards = []
            if "vectorstore" in st.session_state and "text_chunks" in st.session_state and "llm" in st.session_state:
                if st.button("Generează card"):
                    with st.spinner("Generare în curs..."):
                        flashcards = generate_flashcards(
                            st.session_state.text_chunks,
                            st.session_state.llm,
                        )
                        st.session_state.flashcards = flashcards
                        
                        for i, card in enumerate(flashcards):
                            display_flashcard(card, i)
                        st.experimental_rerun()
                if "flashcards" in st.session_state:
                    st.markdown(flashcard_script, unsafe_allow_html=True)
                    for i, card in enumerate(st.session_state.flashcards):
                        flashcard_component(card, key=i)
            else:
                st.warning("Te rog incarca un PDF.")   

if __name__ == '__main__':
    main()