def truncate_text(text: str) -> str:
    if len(text) > 20:
        text = text[0:17] + "..."
    return text