from pdf_parser import read_pdf
from text_splitter import split_text


path = "uploads/A Multimodal Fake News Detection Method Based on Contrastive Learning and Variational Autoencoder(科研通-ablesci.com).pdf"


text = read_pdf(path)

chunks = split_text(text)


print("总字符数:", len(text))

print("chunk数量:", len(chunks))


for i, chunk in enumerate(chunks[:3]):
    print("================")
    print("Chunk", i)
    print(chunk[:300])