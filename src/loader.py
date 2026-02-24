from pathlib import Path
import pandas as pd
from config.settings import SUPPORTED_FORMATS
from src.utils import setup_logger

logger = setup_logger()

class DataLoader:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def validate(self):
        if not self.file_path.exists():
            raise FileNotFoundError(f"{self.file_path} not found")

        if self.file_path.suffix.lower() not in SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format {self.file_path.suffix}"
            )

    def load(self) -> pd.DataFrame:
        self.validate()

        logger.info(f"Loading dataset: {self.file_path}")

        if self.file_path.suffix == ".csv":
            df = pd.read_csv(self.file_path)

        elif self.file_path.suffix == ".xlsx":
            df = pd.read_excel(self.file_path)

        elif self.file_path.suffix == ".json":
            df = pd.read_json(self.file_path)

        else:
            raise ValueError("Unsupported file type")

        logger.info(f"Loaded dataset shape: {df.shape}")
        return df