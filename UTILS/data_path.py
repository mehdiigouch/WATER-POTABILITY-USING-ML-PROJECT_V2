from pathlib import Path
import sys

PROJECT_ROOT = Path.cwd().parent
sys.path.append(str(PROJECT_ROOT))
import pandas as pd


def get_data_path():
    """
    Returns the path to the data directory.
    """
    path = Path.cwd().parent.parent  /"DATASET"/"water_potability.csv"
    return path