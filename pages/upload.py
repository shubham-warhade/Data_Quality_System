import streamlit as st
import pandas as pd

def upload_page():

    st.title("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Choose CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)
        st.session_state.dataset_name = uploaded_file.name

        st.session_state.df = df

        st.success("Dataset uploaded successfully!")

        st.metric("Rows", df.shape[0])

        st.metric("Columns", df.shape[1])

        st.dataframe(df.head())