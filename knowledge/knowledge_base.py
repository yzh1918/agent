import os
from knowledge.text_splitter import split_text
from knowledge.pdf_parser import read_pdf
from knowledge.embedding import embed_texts
from knowledge.vector_store import create_index,save_index,save_chunks


def build_knowledge_base(pdf_path):
    paper_name = os.path.splitext(os.path.basename(pdf_path))[0]
    save_dir=os.path.join("vector_store",paper_name)
    os.makedirs(save_dir, exist_ok=True)
    index_path = os.path.join(save_dir, "index.faiss")
    chunks_path = os.path.join(save_dir, "chunks.json")
    texts = read_pdf(pdf_path)
    chunks = split_text(texts)
    vectors = embed_texts(chunks)
    index = create_index(vectors)
    save_index(index, index_path)
    save_chunks(chunks,chunks_path)
    return paper_name

def list_papers(path):
    papers=[]
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            papers.append(entry)
    return papers

