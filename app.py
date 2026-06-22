import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Rustomjee Sales Strategy Engine by ST",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 CRE Property Description Parser")
st.caption(
    "Upload an IGR Excel file containing Property Description data in Marathi. "
    "The engine will automatically extract and structure property information."
)

# ------------------------
# Import parser modules
# ------------------------

try:
    from parser.column_detector import detect_property_column
    from parser.master_parser import parse_dataframe
    from dashboard.summary import get_summary

except Exception as e:
    st.error(f"Application failed to load: {e}")
    st.stop()

# ------------------------
# File Upload
# ------------------------

uploaded = st.file_uploader(
    "Upload Excel or CSV File",
    type=["xlsx", "xls", "csv"]
)

if uploaded:

    try:

        # ------------------------
        # Read File
        # ------------------------

        if uploaded.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded)

        else:
            df = pd.read_excel(uploaded)

        st.success(
            f"File loaded successfully. Rows detected: {len(df):,}"
        )

        st.subheader("Raw Data Preview")
        st.dataframe(df.head(10))

        # ------------------------
        # Detect Property Description Column
        # ------------------------

        property_col = detect_property_column(df)

        if property_col is None:

            st.error(
                "Property Description column could not be detected automatically."
            )

            st.info(
                "Please ensure your file contains a column named:\n"
                "- Property Description\n"
                "- Description\n"
                "- मालमत्ता वर्णन"
            )

            st.stop()

        st.success(
            f"Property Description Column Detected: {property_col}"
        )

        # ------------------------
        # Parse Button
        # ------------------------

        if st.button("Parse Property Descriptions"):

            with st.spinner(
                "Parsing property descriptions..."
            ):

                result = parse_dataframe(
                    df,
                    property_col
                )

            st.success(
                "Parsing completed successfully."
            )

            # ------------------------
            # Preview
            # ------------------------

            st.subheader("Parsed Data Preview")
            st.dataframe(
                result.head(20),
                use_container_width=True
            )

            # ------------------------
            # Dashboard Metrics
            # ------------------------

            summary = get_summary(result)

            st.subheader("Summary")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Transactions",
                summary["Total Transactions"]
            )

            c2.metric(
                "Average Carpet Area",
                summary["Average Carpet Area"]
            )

            c3.metric(
                "Average Total Area",
                summary["Average Total Area"]
            )

            # ------------------------
            # Download Excel
            # ------------------------

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
                label="📥 Download Parsed Excel",
                data=output.getvalue(),
                file_name="Parsed_Property_Data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:

        st.error(
            f"An error occurred while processing the file:\n{e}"
        )
