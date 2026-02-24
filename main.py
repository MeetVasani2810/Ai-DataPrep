import argparse
from src.loader import DataLoader
from src.utils import setup_logger

logger = setup_logger()

def main():

    parser = argparse.ArgumentParser(
        description="AI DataPrep Engine"
    )

    parser.add_argument(
        "file",
        type=str,
        help="Path to dataset"
    )

    args = parser.parse_args()

    loader = DataLoader(args.file)
    df = loader.load()

    logger.info("Dataset columns:")
    logger.info(list(df.columns))

    logger.info("DataPrep engine initialized successfully.")

if __name__ == "__main__":
    main()