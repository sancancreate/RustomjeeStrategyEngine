import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Rustomjee Sales Strategy Engine",
    layout="wide"
)

st.title("🏢 Rustomjee Sales Strategy Engine")

try:
    from parser.column_detector import detect_property_column
    from parser.master_parser import parse_dataframe
    from dashboard.summary import get_summary

    st.success("✅ All modules imported successfully.")

except Exception as e:
    st.error(f"❌ Import Error: {e}")
    st.stop()
uploaded = st.file_uploader(
    "Upload Excel File",
    type=["xlsx", "xls", "csv"]
)

if uploaded:

    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)

    else:
        df = pd.read_excel(uploaded)

    st.success(
        "File uploaded successfully."
    )

    property_col = detect_property_column(df)

    if property_col is None:

        st.error(
            "Property Description column not found."
        )

    else:

        st.info(
            f"Detected Column: {property_col}"
        )

        if st.button(
            "Parse File"
        ):

            result = parse_dataframe(
                df,
                property_col
            )

            st.success(
                "Parsing completed."
            )

            st.dataframe(
                result.head(20)
            )

            summary = get_summary(
                result
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Transactions",
                summary[
                    "Total Transactions"
                ]
            )

            c2.metric(
                "Average Carpet",
                summary[
                    "Average Carpet Area"
                ]
            )

            c3.metric(
                "Average Total Area",
                summary[
                    "Average Total Area"
                ]
            )

            output = BytesIO()

            with pd.ExcelWriter(
                output,
                engine="xlsxwriter"
            ) as writer:

                result.to_excel(
                    writer,
                    index=False,
                    sheet_name="Parsed Data"
                )

            st.download_button(
                label="Download Parsed Excel",
                data=output.getvalue(),
                file_name="Parsed_Output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
