

def route(question):
    question = question.lower()

    if "summary" in question or "summarize" in question or "总结" in question:
        return "summary"

    return "qa"