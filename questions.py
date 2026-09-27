QUESTIONS = [
    {
        "question": "How are tie-breaks resolved for juniors and seniors in the housing lottery?",
        "expects": "randomly",
    },
    {
        "question": "By what week can you drop a course with a W on your transcript?",
        "expects": "week six",
    },
    {
        "question": "How far in advance should you book an appointment with an adviser before registration opens?",
        "expects": "two weeks",
    },
    {
        "question": "Until what week can you withdraw from a course with an adviser signature?",
        "expects": "week ten",
    },
    {
        "question": "When does adding a course end during the semester?",
        "expects": "second week",
    },
]

OUT_OF_SCOPE = [
    "What is the capital of France?",
    "Where can I buy space shuttle tickets on campus?",
    "Who won the 1998 FIFA World Cup?",
    "What are the basic rules of cricket?",
    "How do I adjust a carburetor on a 1972 Mustang?"
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
