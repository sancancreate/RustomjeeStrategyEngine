import re

SQFT_PATTERN = r'(\d+(?:\.\d+)?)\s*चौ\.\s*फु'


def extract_areas(text):

    result = {
        "carpet_area": None,
        "balcony_area": None,
        "utility_area": None,
        "terrace_area": None,
        "total_area": None
    }

    numbers = re.findall(SQFT_PATTERN, text)

    numbers = [float(x) for x in numbers]

    lower = text.lower()

    if "कार्पेट" in text and len(numbers) >= 1:
        result["carpet_area"] = numbers[0]

    if "बाल्कनी" in text and len(numbers) >= 2:
        result["balcony_area"] = numbers[1]

    if "युटिलिटी" in text and len(numbers) >= 3:
        result["utility_area"] = numbers[2]

    if "टेरेस" in text and len(numbers) >= 4:
        result["terrace_area"] = numbers[3]

    total = 0

    for k in [
        "carpet_area",
        "balcony_area",
        "utility_area",
        "terrace_area"
    ]:
        v = result[k]
        if v:
            total += v

    result["total_area"] = total

    return result
