from pathlib import Path
import sys

PROJECT_ROOT = Path.cwd().parent
sys.path.append(str(PROJECT_ROOT))


from ETL.ETL_PIPELINE import  ETL
from PROCESSING.DATA_PROCESSING import DataProcessor

from UTILS.data_path import get_data_path




path = get_data_path()

data = ETL.run(path)

data.head()
