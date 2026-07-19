import streamlit as st


def about_page():

    st.title("ℹ️ About QualiAI")

    st.markdown("""
# QualiAI – AI Powered Data Quality Assessment System

QualiAI is an AI-powered web application that evaluates the quality of datasets
using Data Profiling, Data Validation, Machine Learning, and Visualization.

## Features

- 📂 Upload CSV Dataset
- 📊 Data Profiling
- ✅ Data Validation
- ⭐ Data Quality Score
- 🤖 Quality Prediction
- 🧹 Smart Data Cleaning
- 🔍 Isolation Forest Anomaly Detection
- 📄 PDF Report Generation
- 💾 Download Cleaned Dataset

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- ReportLab

## Machine Learning Algorithm

Isolation Forest

Isolation Forest detects anomalous records by isolating observations that are
significantly different from the majority of the dataset.

## Developed By

Devis Lilhare
""")