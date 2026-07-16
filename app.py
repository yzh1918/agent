import os
import uvicorn
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from agent.agent import run
from knowledge.vector_store import load_index, load_chunks
from knowledge.knowledge_base import build_knowledge_base,list_papers
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class chatbody(BaseModel):
    paper_name:str
    question:str

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(request:chatbody):
    index_path=os.path.join("vector_store",request.paper_name,"index.faiss")
    chunks_path=os.path.join("vector_store",request.paper_name,"chunks.json")
    index=load_index(index_path)
    chunks=load_chunks(chunks_path)
    answer=run(request.question,index,chunks)
    return {"answer":answer}

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    file_path = os.path.join("uploads",
                             file.filename)
    with open(file_path,"wb") as f:
        content=await file.read()
        f.write(content)
    paper_name=build_knowledge_base(file_path)
    return {"filename":file.filename,
            "paper_name":paper_name,
            "status":"success"}

@app.get("/papers")
def papers():
    papers=list_papers("vector_store")
    return {"papers":papers}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)