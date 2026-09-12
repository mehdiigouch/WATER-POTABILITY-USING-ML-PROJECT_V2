import pandas as pd


class Validation:

    EXPECTED_COLUMNS = {
        "ph",
        "Hardness",
        "Solids",
        "Chloramines",
        "Sulfate",
        "Conductivity",
        "Organic_carbon",
        "Trihalomethanes",
        "Turbidity",
        "Potability"
    }

    EXPECTED_DTYPES = {
        "ph": "float64",
        "Hardness": "float64",
        "Solids": "float64",
        "Chloramines": "float64",
        "Sulfate": "float64",
        "Conductivity": "float64",
        "Organic_carbon": "float64",
        "Trihalomethanes": "float64",
        "Turbidity" :"float64",
        "Potability": "int64"
    }

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def validate_columns(self) -> None:

        source_columns = set(self.df.columns)

        missing_columns = self.EXPECTED_COLUMNS - source_columns
        unexpected_columns = source_columns - self.EXPECTED_COLUMNS

        if missing_columns:
            raise ValueError(
                f"Missing expected columns: {sorted(missing_columns)}"
            )

        if unexpected_columns:
            raise ValueError(
                f"Unexpected columns found: {sorted(unexpected_columns)}"
            )

    def validate_dtypes(self) -> None:

        for column, expected_dtype in self.EXPECTED_DTYPES.items():

            actual_dtype = str(self.df[column].dtype)

            if actual_dtype != expected_dtype:
                raise TypeError(
                    f"{column}: expected {expected_dtype}, "
                    f"got {actual_dtype}"
                )

    def validate(self) -> None:

        self.validate_columns()
        print("[OK] Column validation passed.")

        self.validate_dtypes()
        print("[OK] Data type validation passed.")

        print("[OK] Dataset validation successful.")






