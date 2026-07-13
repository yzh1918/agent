import pickle

from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_parser import read_pdf

def split_text(text,chunk_size=800,chunk_overlap=150):

    text_splitter=RecursiveCharacterTextSplitter(
          chunk_size = chunk_size,
       chunk_overlap = chunk_overlap,
       separators=[
           "\n\n",
           "\n",
           ".",
           "!",
           "?",
           "。",
           " "
       ]
    )
    chunks = text_splitter.split_text(text)
    return chunks
