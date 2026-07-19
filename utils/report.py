import os
import streamlit as st

from utils.report_generator import generate_report


def report_page():

    st.title("📄 Report Generator")

    if st.session_state.df is None:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state.df

    rows = len(df)
    cols = len(df.columns)

    missing = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    summary = {
        "Rows": rows,
        "Columns": cols,
        "Missing Values": missing,
        "Duplicate Rows": duplicates
    }

    st.subheader("Report Summary")

    st.json(summary)

    if st.button("Generate PDF Report"):

        filename = "Data_Quality_Report.pdf"

        generate_report(filename, summary)

        with open(filename, "rb") as file:

            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name=filename,
                mime="application/pdf"
            )

        # Optional cleanup after download is prepared
        if os.path.exists(filename):
            os.remove(filename)