from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))
import pandas as pd


def get_data_path():
    """
    Returns the path to the data directory.
    """
    return Path.cwd().parent /"DATASET"/"water_potability.csv"
    