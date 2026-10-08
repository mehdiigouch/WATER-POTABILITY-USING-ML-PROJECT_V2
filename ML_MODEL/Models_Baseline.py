from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))


from ETL.ETL_PIPELINE import  ETL
from PROCESSING.DATA_PROCESSING import DataProcessor

from UTILS.data_path import Direction


path =Direction().get_data_path()

print(path)



data = ETL.run(path)

data.head()
