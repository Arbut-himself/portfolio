def convert_list_item(markdown: str) -> str:
    if markdown.lstrip()[0].isnumeric() and markdown.lstrip()[1:3] == ". ":
        return f'<li>{markdown.lstrip()[2:].strip()}</li>'
    else:
        return "Invalid format"