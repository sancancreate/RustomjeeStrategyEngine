import re


def extract_parking(text):

    result = {
        "parking_count": 0,
        "parking_number": None,
        "parking_type": None
    }

    parking = re.search(
        r'युनिट नं\.?\s*([A-Za-z0-9\-]+)',
        text
    )

    if parking:
        result["parking_count"] = 1
        result["parking_number"] = parking.group(1)

    if "पोडीयम" in text:
        result["parking_type"] = "Podium"

    elif "बेसमेंट" in text:
        result["parking_type"] = "Basement"

    return result
