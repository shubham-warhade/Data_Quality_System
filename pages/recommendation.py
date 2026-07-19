import streamlit as st
from utils.cleaner import DataCleaner

def recommendation_page():

    st.title("🧹 Smart Data Cleaning")

    if st.session_state.df is None:
        st.warning("Please upload a dataset first.")
        return

    cleaner = DataCleaner(st.session_state.df)

    st.subheader("Select Cleaning Operations")

    remove_duplicates = st.checkbox("Remove Duplicate Rows")
    fill_numeric = st.checkbox("Fill Missing Numeric Values")
    fill_categorical = st.checkbox("Fill Missing Categorical Values")
    remove_constant = st.checkbox("Remove Constant Columns")

    if st.button("🧹 Clean Dataset"):

        if remove_duplicates:
            cleaner.remove_duplicates()

        if fill_numeric:
            cleaner.fill_numeric()

        if fill_categorical:
            cleaner.fill_categorical()

        removed_cols = []

        if remove_constant:
            removed_cols = cleaner.remove_constant_columns()

        cleaned_df = cleaner.get_dataframe()

        st.session_state.cleaned_df = cleaned_df

        st.success("Dataset cleaned successfully!")

        st.write("### Cleaned Dataset")

        st.dataframe(cleaned_df.head())

        csv = cleaned_df.to_csv(index=False)

        st.download_button(
            label="⬇ Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )

        if removed_cols:
            st.info(f"Removed Constant Columns: {', '.join(removed_cols)}")