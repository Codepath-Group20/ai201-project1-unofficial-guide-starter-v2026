def judge(question: str, expects: str, answer: str, results: list) -> bool:
    if not expects:
        return False
        
    # Standard check: does the generated answer contain the expected fallback text?
    return expects.lower() in answer.lower()
