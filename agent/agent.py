from knowledge.retriever import retriever
from llm import chat
from router import route

def run(question,index,chunks):
        task=route(question)
        context=retriever(question,index,chunks)
        answer=chat(task,question,context)
        return answer


