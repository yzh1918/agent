from retriever import retriever
from vector_store import *
from llm import chat


chunks = load_chunks("./vector_store/chunks.json")


index=load_index("./vector_store/index")

question = "What is the innovation of this paper?"

context=retriever(question,index,chunks)

answer=chat(question,context)

print(answer)



