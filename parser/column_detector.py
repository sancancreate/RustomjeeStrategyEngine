def detect_property_column(df):

    possible = [
        "property description",
        "description",
        "property details",
        "marathi description",
        "मालमत्ता वर्णन",
        "इतर वर्णन"
    ]

    for col in df.columns:

        c = str(col).lower().strip()

        for p in possible:

            if p.lower() in c:
                return col

    return None
