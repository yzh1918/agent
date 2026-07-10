import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class chatbody(BaseModel):
    question:str

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(request:chatbody):
    return {"answer":request.question}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)