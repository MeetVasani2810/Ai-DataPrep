from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Report paths
REPORTS_DIR = BASE_DIR / "reports"
PROFILE_DIR = REPORTS_DIR / "profile"
PLOTS_DIR = REPORTS_DIR / "plots"

# Logging
LOG_LEVEL = "INFO"

# Supported file types
SUPPORTED_FORMATS = [".csv", ".xlsx", ".json"]from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Report paths
REPORTS_DIR = BASE_DIR / "reports"
PROFILE_DIR = REPORTS_DIR / "profile"
PLOTS_DIR = REPORTS_DIR / "plots"

# Logging
LOG_LEVEL = "INFO"

# Supported file types
SUPPORTED_FORMATS = [".csv", ".xlsx", ".json"]

# This file is used to store the settings for the application