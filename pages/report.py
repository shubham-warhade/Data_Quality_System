import streamlit as st
from utils.report_generator import generate_report
from datetime import datetime


def report_page():

    st.title("📄 AI Data Quality Report")

    if st.session_state.df is None:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state.df

    quality_score = st.session_state.get("quality_score", 0)
    anomaly_count = st.session_state.get("anomaly_count", 0)

    # -----------------------------
    # Dataset Summary
    # -----------------------------
    summary = {
        "Report Date": datetime.now().strftime("%d-%b-%Y %H:%M"),
        "Dataset Name": st.session_state.get("dataset_name", "Unknown"),
        "Rows": len(df),
        "Columns": len(df.columns),
        "Quality Score": f"{quality_score}%",
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Anomalies Detected": anomaly_count
    }

    # -----------------------------
    # AI Recommendations
    # -----------------------------
    recommendations = []

    if df.isnull().sum().sum() > 0:
        recommendations.append("Fill missing values to improve data quality.")

    if df.duplicated().sum() > 0:
        recommendations.append("Remove duplicate rows.")

    if anomaly_count > 0:
        recommendations.append("Review anomalous records detected by the ML model.")

    if quality_score >= 90:
        recommendations.append("Dataset quality is excellent.")

    elif quality_score >= 75:
        recommendations.append("Dataset quality is good with minor improvements required.")

    else:
        recommendations.append("Dataset requires cleaning before further analysis.")

    # -----------------------------
    # Show Report Preview
    # -----------------------------
    st.subheader("📋 Report Summary")

    for key, value in summary.items():
        st.write(f"**{key}:** {value}")

    st.subheader("💡 Recommendations")

    for rec in recommendations:
        st.write(f"• {rec}")

    # -----------------------------
    # Generate PDF
    # -----------------------------
    if st.button("📄 Generate PDF Report"):

        filename = "Quality_Report.pdf"

        generate_report(
            summary,
            recommendations,
            filename
        )

        st.success("✅ PDF Report Generated Successfully!")

        with open(filename, "rb") as pdf:
            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf,
                file_name=filename,
                mime="application/pdf"
            )