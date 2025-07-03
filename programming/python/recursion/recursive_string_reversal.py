def string_rev(text: str) -> str:
    if len(text) == 0:
        return ""
    return string_rev(text[1:]) + text[0]

text = "five am study rocks!"
print(string_rev(text))