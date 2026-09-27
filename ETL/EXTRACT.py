from pathlib import Path

import pandas as pd


class EXTRACTION:
    """Extract data from a CSV source."""

    def __init__(
        self,
        source_path: str | Path,
        encoding: str = "utf-8"
    ):
        self.source_path = Path(source_path)
        self.encoding = encoding

    def run(self) -> pd.DataFrame:
        """Read the CSV source and return a DataFrame."""

        if not self.source_path.is_file():
            raise FileNotFoundError(
                f"Source file does not exist: {self.source_path}"
            )

        try:
            data = pd.read_csv(
                self.source_path,
                encoding=self.encoding
            )

            return data

        except pd.errors.ParserError as exc:
            raise ValueError(
                f"Unable to parse CSV file: {self.source_path}"
            ) from exc

        except UnicodeDecodeError as exc:
            raise ValueError(
                f"Unable to decode file '{self.source_path}' "
                f"using encoding '{self.encoding}'."
            ) from exc