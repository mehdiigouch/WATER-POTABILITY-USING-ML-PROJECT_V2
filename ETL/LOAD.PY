import pandas as pd

class Load:

    def __init__(self, df: pd.DataFrame, output_path: str):
        self.df = df
        self.output_path = output_path

    def load(self) -> None:
        self.df.to_csv(self.output_path, index=False)

        print(
            f"[OK] Data successfully loaded to {self.output_path}"
        )
