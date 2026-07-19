import pandas as pd

class DataCleaner:

    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def fill_numeric(self):
        numeric_cols = self.df.select_dtypes(include=["number"]).columns
        for col in numeric_cols:
            self.df[col] = self.df[col].fillna(self.df[col].median())

    def fill_categorical(self):
        categorical_cols = self.df.select_dtypes(exclude=["number"]).columns
        for col in categorical_cols:
            if not self.df[col].mode().empty:
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

    def remove_constant_columns(self):
        constant_cols = [
            col for col in self.df.columns
            if self.df[col].nunique(dropna=False) == 1
        ]
        self.df = self.df.drop(columns=constant_cols)
        return constant_cols

    def get_dataframe(self):
        return self.df