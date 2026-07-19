import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def profiling_page():

    st.title("📊 Data Profiling")

    if st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.df

    # ==========================
    # Basic Statistics
    # ==========================

    rows = df.shape[0]
    columns = df.shape[1]

    missing = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    memory = round(df.memory_usage(deep=True).sum() / 1024, 2)

    numerical = len(df.select_dtypes(include=np.number).columns)

    categorical = len(df.select_dtypes(exclude=np.number).columns)

    st.subheader("Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", rows)
    c2.metric("Columns", columns)
    c3.metric("Memory (KB)", memory)

    c4, c5, c6 = st.columns(3)

    c4.metric("Missing Values", missing)
    c5.metric("Duplicate Rows", duplicates)
    c6.metric("Numerical Columns", numerical)

    st.metric("Categorical Columns", categorical)

    st.divider()

    # ==========================
    # Data Types
    # ==========================

    st.subheader("Column Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(dtype_df, use_container_width=True)

    st.divider()

    # ==========================
    # Missing Values
    # ==========================

    st.subheader("Missing Values")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isnull().sum(),
        "Missing %": round(df.isnull().mean() * 100, 2)
    })

    st.dataframe(missing_df, use_container_width=True)

    st.divider()

    # ==========================
    # Statistical Summary
    # ==========================

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(include="all").fillna(""),
        use_container_width=True
    )

    st.divider()

    # ==========================
    # Dataset Preview
    # ==========================

    st.subheader("Dataset Preview")

    st.divider()

    st.subheader("📊 Missing Values by Column")

    missing_chart = pd.DataFrame({
        "Column": df.columns,
        "Missing": df.isnull().sum().values
    })

    fig = px.bar(
        missing_chart,
        x="Column",
        y="Missing",
        title="Missing Values"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("🥧 Data Type Distribution")

    dtype_counts = df.dtypes.astype(str).value_counts()

    fig = px.pie(
        values=dtype_counts.values,
        names=dtype_counts.index,
        title="Column Data Types"
    )

    st.plotly_chart(fig, use_container_width=True)

    numeric_cols = df.select_dtypes(include=np.number).columns

    if len(numeric_cols) > 0:
        st.divider()

        st.subheader("📈 Histogram")

        selected_col = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig = px.histogram(
            df,
            x=selected_col,
            nbins=30,
            title=f"{selected_col} Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        if len(numeric_cols) > 0:
            st.divider()

            st.subheader("📦 Outlier Detection")

            selected_box = st.selectbox(
                "Select Column for Box Plot",
                numeric_cols,
                key="box"
            )

            fig = px.box(
                df,
                y=selected_box,
                title=f"Outlier Detection - {selected_box}"
            )

            st.plotly_chart(fig, use_container_width=True)

            if len(numeric_cols) > 1:
                st.divider()

                st.subheader("🔥 Correlation Heatmap")

                corr = df[numeric_cols].corr()

                fig = px.imshow(
                    corr,
                    text_auto=True,
                    aspect="auto",
                    title="Correlation Matrix"
                )

                st.plotly_chart(fig, use_container_width=True)



    st.dataframe(df.head(20), use_container_width=True)