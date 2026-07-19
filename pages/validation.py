import streamlit as st
import pandas as pd
import numpy as np

def validation_page():

    st.title("✅ Data Validation")

    if st.session_state.df is None:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state.df

    total_rows = len(df)
    total_columns = len(df.columns)
    total_cells = total_rows * total_columns

    # -------------------------
    # Missing Values
    # -------------------------
    missing_count = df.isnull().sum().sum()
    missing_percent = round((missing_count / total_cells) * 100, 2)

    # -------------------------
    # Duplicate Rows
    # -------------------------
    duplicate_count = df.duplicated().sum()
    duplicate_percent = round((duplicate_count / total_rows) * 100, 2)

    # -------------------------
    # Empty Strings
    # -------------------------
    empty_strings = (
        df.astype(str)
          .apply(lambda col: col.str.strip() == "")
          .sum()
          .sum()
    )

    # -------------------------
    # Constant Columns
    # -------------------------
    constant_columns = []

    for col in df.columns:
        if df[col].nunique(dropna=False) == 1:
            constant_columns.append(col)

    # -------------------------
    # Quality Score
    # -------------------------
    quality_score = 100

    quality_score -= min(missing_percent, 40)
    quality_score -= min(duplicate_percent, 20)
    quality_score -= len(constant_columns) * 5

    quality_score = max(0, round(quality_score, 2))
    st.session_state.quality_score = quality_score
    st.write("Saved Quality Score:", st.session_state.quality_score)

    # -------------------------
    # Dashboard
    # -------------------------

    c1, c2, c3 = st.columns(3)

    c1.metric("Quality Score", f"{quality_score}%")
    c2.metric("Missing %", f"{missing_percent}%")
    c3.metric("Duplicate %", f"{duplicate_percent}%")

    st.divider()

    st.subheader("Validation Summary")

    summary = pd.DataFrame({
        "Validation": [
            "Missing Values",
            "Duplicate Rows",
            "Empty Strings",
            "Constant Columns"
        ],
        "Result": [
            missing_count,
            duplicate_count,
            empty_strings,
            len(constant_columns)
        ]
    })

    st.dataframe(summary, use_container_width=True)

    if constant_columns:

        st.subheader("Constant Columns")

        st.write(constant_columns)

    else:

        st.success("No constant columns found.")

