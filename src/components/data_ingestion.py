import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging  # Ensure logging is set up properly

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        try:
            logging.info("Initiating data ingestion")

            # Read the dataset
            self.data = pd.read_csv(self.config.raw_data_path)
            logging.info(f"Data loaded successfully from {self.config.raw_data_path}")

            # Ensure artifact directories exist
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.config.test_data_path), exist_ok=True)

            # Save raw data
            self.data.to_csv(self.config.raw_data_path, index=False, header=True)

            # Split data
            logging.info("Train Test Split initiated")
            train_set, test_set = train_test_split(self.data, test_size=0.2, random_state=42)

            # Save train and test datasets
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info(f"Data ingestion completed. Train data saved at {self.config.train_data_path}, Test data saved at {self.config.test_data_path}")

            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            logging.error(f"Data ingestion failed with error: {e}")
            raise CustomException(e, sys)  # Pass sys for traceback details

if __name__ == "__main__":
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config)
    data_ingestion.initiate_data_ingestion()
