import faiss

def create_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index

def save_index(index,path):
    faiss.write_index(index,path)

def load_index(path):
    index=faiss.read_index(path)
    return index

def search_index(index, query_vector, top_k=5):
    D,I=index.search(query_vector, top_k)
    return D,I

import json

def save_chunks(chunks, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False)

def load_chunks(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)