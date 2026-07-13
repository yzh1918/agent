from openai import OpenAI
from config import DEEPSEEK_API_KEY

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com")



def build_propmt(question,context):
    context_text="\n\n".join(context)
    prompt=f"""You are an academic paper assistant.Answer the question only according to the following context.
            
            Context:{context_text}
            
            Question:{question}
            
            Answer:"""
    return prompt

def chat(question,context):
    prompt=build_propmt(question,context)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}})
    return response.choices[0].message.content
