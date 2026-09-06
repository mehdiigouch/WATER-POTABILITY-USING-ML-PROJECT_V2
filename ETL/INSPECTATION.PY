import pandas as pd
from EXTRACT import Extraction
from pathlib import Path


DATA = Path.cwd().parent.parent  /"WATER"/"DATASET"/"water_potability.csv"



class Inspection:

    def __init__(self,path):
        self.path=path


    def inspect_data(self):

        data = Extraction(self.path).extract_data()

        print("Data Inspection: start" ,data.head())

        #  shape  -  datatype  -   column names  -  first 5 rows head & tail - % of messing values
        # duplicate rows & columns


        










Inspection(DATA).inspect_data()







