import pandas as pd


class TRANSFORMATION:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()




    def standardize_columns(self) -> pd.DataFrame:
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return self.df



    

    