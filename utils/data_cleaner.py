import pandas as pd


def clean_dataset(df):
    """
    Automatically clean the dataset.
    """

    cleaned = df.copy()

    # Remove duplicate rows
    cleaned = cleaned.drop_duplicates()

    # Fill numeric missing values
    numeric_cols = cleaned.select_dtypes(include="number").columns

    for col in numeric_cols:
        cleaned[col] = cleaned[col].fillna(cleaned[col].median())

    # Fill categorical missing values
    categorical_cols = cleaned.select_dtypes(exclude="number").columns

    for col in categorical_cols:
        mode = cleaned[col].mode()

        if len(mode) > 0:
            cleaned[col] = cleaned[col].fillna(mode[0])

    return cleaned