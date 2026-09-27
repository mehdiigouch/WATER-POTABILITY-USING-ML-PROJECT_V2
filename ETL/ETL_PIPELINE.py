
from pathlib import Path

import pandas as pd

from EXTRACT import EXTRACTION
from TRANSFORMATION import TRANSFORMATION
from LOAD import LOAD


class ETL:
    

    @classmethod
    def pipeline(
        cls,
        source_path: str | Path,
        output_path: str | Path | None = None
    ) -> pd.DataFrame:

        # 1. Extract
        raw_df = EXTRACTION(source_path).run()

        # 2. Transform
        transformed_df = (
            TRANSFORMATION(raw_df)
            .run()
        )

        # 3. Load only if an output path was provided
        if output_path is not None:
            LOAD(
                transformed_df,
                output_path
            ).run()

        # 4. Return the final DataFrame
        return transformed_df