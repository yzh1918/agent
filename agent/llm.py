from openai import OpenAI
from config import DEEPSEEK_API_KEY

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com")

TASK_PROMPTS = {
    "qa": (
        "You are an academic paper assistant. "
        "Answer the user's question only according to the provided context. "
        "If the answer cannot be found in the context, say you don't know."
    ),

    "summary": (
        "You are an academic paper assistant. "
        "Please summarize this paper according to the provided context. "
        "Include the research background, proposed method, experiments, and conclusions."
    )
}


def build_prompt(task,question,context):
    instruction = TASK_PROMPTS[task]
    context_text = "\n\n".join(context)
    if question:
        context_text = "\n\n".join(context)
        prompt = f"""{instruction}.

                    Context:{context_text}
                    Question:{question}
                    Answer:"""
    else:
        prompt=f"""{instruction}.
            
                Context:{context_text}
            
                Answer:"""
    return prompt

def chat(task,question,context):
    prompt=build_prompt(task,question,context)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}})
    return response.choices[0].message.content
