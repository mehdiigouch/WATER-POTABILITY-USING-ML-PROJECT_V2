import pandas as pd



import pandas as pd


class TRANSFORMATION:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def standardize_columns(self) -> pd.Index:
        standardized_columns = (
            self.df.columns
            .astype(str)
            .str.strip()
            .str.lower()
            .str.replace(r"\s+", "_", regex=True)
            .str.replace(r"_+", "_", regex=True)
            .str.strip("_")
        )

        return standardized_columns

    def duplicate_checker(self, standardized_columns: pd.Index) -> None:
        duplicates = standardized_columns[
            standardized_columns.duplicated()
        ].tolist()

        if duplicates:
            raise ValueError(
                f"Duplicate column names after standardization: {duplicates}"
            )

    def run(self) -> pd.DataFrame:
        standardized_columns = self.standardize_columns()

        self.duplicate_checker(standardized_columns)

        self.df.columns = standardized_columns

        return self.df


