from pathlib import Path
from PyPDF2 import PdfReader
from typing import IO
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf) # creeaza obiectul pdf care are pagini
        for page in pdf_reader.pages:
            text += page.extract_text() # se extrage tot textul din documentele PDF
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 150,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks