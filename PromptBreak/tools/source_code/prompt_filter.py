# prompt_filter.py

def is_prompt_injection(text):
    # Basic list of keywords that often appear in jailbreaks
    suspicious_keywords = [
        "ignore", "override", "forget", "bypass", "disregard",
        "act as", "redefine", "break", "unfiltered", "no restrictions"
    ]
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in suspicious_keywords)
