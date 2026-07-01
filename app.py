import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain
from dotenv import load_dotenv

#loading environment variable(api keys)
load_dotenv()

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks=text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def main():
    st.set_page_config(page_title="Chat with PDFs",page_icon="📚")
    st.header("Chat with multiple PDFs: books:")
    if "messages" not in st.session_state:
        st.session_state.messages=[]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs=st.file_uploader("Upload your files here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                st.session_state.vector_store=get_vector_store(text_chunks)
                st.success("Done! you can ask questions now.")
    
    if user_question :=st.chat_input("Ask a question about your documents"):
        st.session_state.messages.append({"role":"user","content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)
        if "vector_store" in st.session_state:
            docs=st.session_state.vector_store.similarity_search(user_question)
            llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)
            chain=load_qa_chain(llm,chain_type="stuff")
            with st.spinner("Thinking..."):
                response = chain.run(input_documents=docs, question=user_question)

            st.session_state.messages.append({"role":"assistant","content":response})
            with st.chat_message("assistant"):
                st.markdown(response)
        else:
            st.warning("please upload and process the pdf first.")


if __name__ == '__main__':
    main()