from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))
import pandas as pd





class Direction : 

        def __init__(self):
            self.path = Path.cwd().parent /"DATASET"/"water_potability.csv"


        def get_data_path(self):
            """
            Returns the path to the data directory.
            """
            return self.path


        def path_for_notebooks(self):
            """
            Returns the path to the data directory for notebooks.
            """
            self.path = Path.cwd().parent.parent / "DATASET"/"water_potability.csv"
            return self.path