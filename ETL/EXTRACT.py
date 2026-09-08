
import pandas as pd
from pathlib import Path



#Path.cwd().parent  /"DATASET"/"water_potability.csv"


class Extraction:
    def __init__(self, source_path):
        self.source_path = source_path

    def extract_data(self) -> pd.DataFrame:
        
        try:
            # Check if the source path exists
            if not Path(self.source_path).exists():
                
                raise FileNotFoundError(f"Source path {self.source_path} does not exist.")

            # Read the data into a DataFrame
            data = pd.read_csv(self.source_path)
            
            return data

        except Exception as e:
            
            raise




