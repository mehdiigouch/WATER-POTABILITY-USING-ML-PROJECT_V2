
from pathlib import Path

import pandas as pd

from EXTRACT import EXTRACTION
from TRANSFORMATION import TRANSFORMATION
from LOAD import LOAD
from VALIDATION import Validation
from INSPECTATION import  Inspection


class ETL:
    

    @classmethod
    def pipeline(
        cls,
        source_path: str | Path,
        output_path: str | Path | None = None
    ) -> pd.DataFrame:

        # 1. Extract & validation
        raw_df = EXTRACTION(source_path).run()

        Validation(raw_df).run()


        # 2. Transform & inspection
        transformed_df = (
            TRANSFORMATION(raw_df)
            .run()
        )

        Inspection(transformed_df).inspect_data()

        # 3. Load only if an output path was provided
        if output_path is not None:
            LOAD(
                transformed_df,
                output_path
            ).run()

        # 4. Return the final DataFrame
        return transformed_df