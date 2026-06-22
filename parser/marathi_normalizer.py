import re

MARATHI_DIGITS = str.maketrans(
    "०१२३४५६७८९",
    "0123456789"
)


def normalize_text(text):

    if text is None:
        return ""

    text = str(text)

    text = text.translate(MARATHI_DIGITS)

    text = re.sub(r"\s+", " ", text)

    return text.strip()
