
# creating class  Extraction , to extarct data from the source and pass it to the next step of 
# the pipeline 


from logging import log
from pathlib import path
import pandas as pd


class Extraction:
    def __init__(self, source_path: str):
        self.source_path = source_path

    def extract_data(self) -> pd.DataFrame:
        """
        Extracts data from the source path and returns it as a pandas DataFrame.

        Returns:
            pd.DataFrame: The extracted data.
        """
        try:
            # Check if the source path exists
            if not path.Path(self.source_path).exists():
                log.error(f"Source path {self.source_path} does not exist.")
                raise FileNotFoundError(f"Source path {self.source_path} does not exist.")

            # Read the data into a DataFrame
            data = pd.read_csv(self.source_path)
            log.info(f"Data extracted successfully from {self.source_path}.")
            return data

        except Exception as e:
            log.error(f"An error occurred while extracting data: {e}")
            raise