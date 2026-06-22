import re


def extract_project(text):

    result = {
        "project_name": None,
        "building_name": None
    }

    project = re.search(
        r'प्रोजेक्ट मधील (.*?) बिल्डिंग',
        text
    )

    if project:
        result["project_name"] = project.group(1).strip()

    building = re.search(
        r'([A-Za-zअ-ह ]+) बिल्डिंग',
        text
    )

    if building:
        result["building_name"] = building.group(1).strip()

    return result
