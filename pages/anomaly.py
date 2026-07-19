import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import plotly.express as px



def anomaly_page():

    st.title("🧠 ML Anomaly Detection")

    if st.session_state.df is None:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state.df.copy()

    # Keep only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        st.error("No numeric columns found.")
        return

    # Fill missing values
    numeric_df = numeric_df.fillna(numeric_df.mean())

    contamination = st.slider(
        "Expected Outlier Percentage",
        0.01,
        0.20,
        0.05,
        0.01
    )

    model = IsolationForest(
        contamination=contamination,
        random_state=42
    )

    prediction = model.fit_predict(numeric_df)

    df["Anomaly"] = prediction

    anomalies = df[df["Anomaly"] == -1]
    st.session_state.anomaly_count = len(anomalies)
    normal = df[df["Anomaly"] == 1]

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Records", len(df))
    c2.metric("Normal Records", len(normal))
    c3.metric("Anomalies", len(anomalies))

    st.divider()

    st.subheader("Detected Anomalies")

    st.dataframe(anomalies)

    st.divider()

    anomaly_percentage = round((len(anomalies) / len(df)) * 100, 2)

    st.metric("Anomaly Percentage", f"{anomaly_percentage}%")

    st.divider()

    st.subheader("Anomaly Visualization")
    st.info("Select any two numeric columns to visualize anomalies.")

    numeric_cols = numeric_df.columns.tolist()

    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("X Axis", numeric_cols)

        y_axis = st.selectbox("Y Axis", numeric_cols, index=1)

        fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            color=df["Anomaly"].astype(str),
            color_discrete_map={
                "1": "blue",
                "-1": "red"
            },
            labels={
                "1": "Normal",
                "-1": "Anomaly"
            },
            title="Isolation Forest Anomaly Detection"
        )

        st.plotly_chart(fig, use_container_width=True)

    csv = anomalies.to_csv(index=False)

    st.download_button(
        "⬇ Download Anomalies",
        csv,
        "anomalies.csv",
        "text/csv"
    )