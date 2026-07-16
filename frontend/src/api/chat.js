import axios from "axios";

export function chat(paperName,question){
    return axios.post("http://127.0.0.1:8000/chat",
    {paper_name:paperName,
          question:question});

}