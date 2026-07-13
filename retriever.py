from agent.embedding import embed_texts

from agent.vector_store import search_index


def retriever(question,index,chunks,top_k=5):
    query_vector=embed_texts(question)
    retrieved_chunks = []
    D,I=search_index(index,query_vector,top_k)
    for idx in I[0]:
        retrieved_chunks.append(chunks[idx])
    return retrieved_chunks