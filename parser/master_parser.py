import pandas as pd

from parser.marathi_normalizer import normalize_text
from parser.area_extractor import extract_areas
from parser.project_extractor import extract_project
from parser.unit_extractor import extract_unit
from parser.parking_extractor import extract_parking
from parser.legal_extractor import extract_legal


def parse_dataframe(df, property_col):

    rows = []

    for _, row in df.iterrows():

        text = normalize_text(
            row[property_col]
        )

        data = {}

        data.update(
            extract_areas(text)
        )

        data.update(
            extract_project(text)
        )

        data.update(
            extract_unit(text)
        )

        data.update(
            extract_parking(text)
        )

        data.update(
            extract_legal(text)
        )

        rows.append(data)

    parsed = pd.DataFrame(rows)

    return pd.concat(
        [df.reset_index(drop=True),
         parsed.reset_index(drop=True)],
        axis=1
    )
