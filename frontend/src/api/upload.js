import axios from "axios";

export function uploadPdf(file){
    const formData=new FormData();
    formData.append("file",file)
    return axios.post(
        "http://127.0.0.1:8000/upload",
        formData
    )
}