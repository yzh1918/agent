import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    r"D:\project\agent\models\bge-m3",
    local_files_only=True
)

def embed_texts(chunks):
    if isinstance(chunks, str):
        chunks = [chunks]
    embeddings = model.encode(chunks)

    return embeddings
    