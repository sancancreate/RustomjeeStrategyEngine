import re


def extract_legal(text):

    result = {
        "rera_number": None,
        "survey_number": None
    }

    rera = re.search(
        r'(P\d{11})',
        text
    )

    if rera:
        result["rera_number"] = rera.group(1)

    survey = re.search(
        r'स\.नं\.\s*(.*?)\s*वरील',
        text
    )

    if survey:
        result["survey_number"] = survey.group(1)

    return result
