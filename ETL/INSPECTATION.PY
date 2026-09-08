import pandas as pd

class Inspection:

    def __init__(self, df: pd.DataFrame):
        self.data = df

    def inspect_data(self):

        print("=" * 70)
        print("                 DATASET INSPECTION REPORT")
        print("=" * 70)

        # ==================================================
        # GENERAL INFORMATION
        # ==================================================

        print("\nGENERAL INFORMATION")
        print("-" * 70)

        dimensions = self.data.shape
        rows, columns = self.data.shape

        # Duplicate rows
        duplicate_rows = self.data.duplicated().sum()

        duplicate_rows_percentage = (
            duplicate_rows / len(self.data) * 100
        )

        # Missing values per column
        missing_count = self.data.isnull().sum()

        missing_percentage = (
            self.data.isnull()
            .mean()
            .mul(100)
            .round(2)
            .sort_values(ascending=False)
        )

        # Duplicate values per column
        duplicate_values_percentage = (
            self.data
            .apply(lambda col: col.duplicated().mean() * 100)
            .round(2)
            .sort_values(ascending=False)
        )

        # Duplicated columns
        duplicate_columns = self.data.T.duplicated()

        # Data types
        data_types = self.data.dtypes

        # Non-missing values
        non_missing_values = self.data.notnull().sum()

        print(f"Dimensions             : {dimensions}")
        print(f"Rows                   : {rows:,}")
        print(f"Columns                : {columns:,}")
        print(f"Duplicate Rows         : {duplicate_rows:,}")
        print(f"Duplicate Rows (%)     : {duplicate_rows_percentage:.2f}%")

        # ==================================================
        # COLUMN INFORMATION
        # ==================================================

        print("\nCOLUMN INFORMATION")
        print("-" * 70)

        column_info = pd.DataFrame({
            "Data Type": data_types,
            "Non-Missing": non_missing_values,
            "Missing": missing_count,
            "Missing %": missing_percentage,
            "Duplicate Values %": duplicate_values_percentage,
            "Duplicated Column": duplicate_columns
        })

        print(column_info.to_string())

        # ==================================================
        # SAMPLE DATA
        # ==================================================

        print("\nSAMPLE OF THE DATASET")
        print("-" * 70)

        print("\nFirst 5 rows:")
        print(self.data.head().to_string())

        print("\nLast 5 rows:")
        print(self.data.tail().to_string())

        # ==================================================
        # STATISTICS
        # ==================================================

        print("\nSTATISTICAL SUMMARY")
        print("-" * 70)

        print(self.data.describe().to_string())

        print("\n" + "=" * 70)
        print("                  END OF REPORT")
        print("=" * 70)
     