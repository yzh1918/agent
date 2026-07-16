from knowledge.retriever import retriever
from knowledge.vector_store import load_chunks,load_index
from agent.llm import chat
import os
pdf_name="FauxBuster_A_Content_free_Fauxtography_D"
chunks = load_chunks(os.path.join("../vector_store",pdf_name,"chunks.json"))
index = load_index(os.path.join("../vector_store",pdf_name,"index"))



question = "What is the innovation of this paper?"

context=retriever(question,index,chunks)

answer=chat("qa",question,context)

print(answer)



