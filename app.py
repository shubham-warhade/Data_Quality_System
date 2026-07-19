import streamlit as st

from pages.dashboard import dashboard_page
from pages.upload import upload_page
from pages.profiling import profiling_page
from pages.validation import validation_page
from pages.anomaly import anomaly_page
from pages.recommendation import recommendation_page
from pages.report import report_page
from pages.prediction import prediction_page
from pages.about import about_page

st.set_page_config(
    page_title="QualiAI",
    page_icon="🤖",
    layout="wide"
)

if "df" not in st.session_state:
    st.session_state.df = None

st.sidebar.title("🤖 QualiAI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload Dataset",
        "Data Profiling",
        "Validation",
        "ML Anomaly Detection",
        "Dataset Quality Prediction",
        "Recommendations",
        "Report"
    ]
)

if menu == "Dashboard":
    dashboard_page()

elif menu == "Upload Dataset":
    upload_page()

elif menu == "Data Profiling":
    profiling_page()

elif menu == "Validation":
    validation_page()

elif menu == "ML Anomaly Detection":
    anomaly_page()

elif menu == "Dataset Quality Prediction":
    prediction_page()

elif menu == "Recommendations":
    recommendation_page()

elif menu == "Report":
    report_page()

elif menu == "About":
    about_page()
