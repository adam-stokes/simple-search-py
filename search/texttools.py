import string

def normalize(text):
    """Normalizes the text"""

    # lower case string
    text = text.lower().strip()

    # remove punctuation
    for ch in text:
        if ch in string.punctuation:
            text = text.replace(ch, "")
    return text
