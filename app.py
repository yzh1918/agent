import os
import uvicorn
from fastapi import FastAPI,UploadFile,File
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

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    file_path = os.path.join("uploads",
                             file.filename)
    with open(file_path,"wb") as f:
        content=await file.read()
        f.write(content)

    return {"filename":file.filename,
            "status":"success"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)