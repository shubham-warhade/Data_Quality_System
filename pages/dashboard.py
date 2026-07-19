import streamlit as st
import plotly.graph_objects as go

from utils.dashboard import metric_card

def dashboard_page():

    st.title("🤖 QualiAI")
    st.info("""
    QualiAI is an AI-powered Data Quality Assessment System that helps users:

    • Analyze datasets
    • Detect missing values
    • Identify duplicates
    • Detect anomalies using Machine Learning
    • Generate quality reports
    • Download cleaned datasets
    """)
    
    st.sidebar.success("Project Status: Ready")

    st.sidebar.markdown("### Features")

    st.sidebar.write("✅ Upload CSV")
    st.sidebar.write("✅ Data Profiling")
    st.sidebar.write("✅ Data Validation")
    st.sidebar.write("✅ Quality Score")
    st.sidebar.write("✅ Smart Cleaning")
    st.sidebar.write("✅ ML Anomaly Detection")
    st.sidebar.write("✅ PDF Report")

    st.subheader("AI Powered Data Quality Assessment System")

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    if st.session_state.df is not None:

        if st.session_state.df is not None:
            df = st.session_state.df

            quality_score = st.session_state.get("quality_score", "N/A")

            c1.metric("Datasets", 1)
            c2.metric("Rows", df.shape[0])
            c3.metric("Columns", df.shape[1])
            c4.metric("Quality Score", f"{quality_score}%")

    else:

        c1.metric("Datasets", 0)
        c2.metric("Rows", 0)
        c3.metric("Columns", 0)
        c4.metric("Quality Score", "--")

    st.info("Upload a dataset to begin analysis.")

    st.divider()

    st.subheader("Dataset Quality Score")

    quality_score = st.session_state.get("quality_score", 0)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=quality_score,
            title={"text": "Quality Score"},

            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 50], "color": "red"},
                    {"range": [50, 80], "color": "yellow"},
                    {"range": [80, 100], "color": "lightgreen"}
                ]
            }
        )
    )

    st.plotly_chart(fig, use_container_width=True)