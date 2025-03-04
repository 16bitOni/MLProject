import logging
import os
from datetime import datetime

# Define log file name and path
LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd(), LOG_DIR)

# Ensure the directory exists
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Test logging
if __name__ == "__main__":
    logging.info("This is a test log message")
    logging.error("This is a test error message")
    logging.warning("This is a test warning message")
    logging.critical("This is a test critical message")
