import re


def extract_unit(text):

    result = {
        "unit_number": None,
        "floor": None
    }

    unit = re.search(
        r'सदनिका नं\.?\s*(\S+)',
        text
    )

    if unit:
        result["unit_number"] = unit.group(1)

    floor = re.search(
        r'([^\s]+)\s*मजला',
        text
    )

    if floor:
        result["floor"] = floor.group(1)

    return result
