import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.Ingestion_config = DataIngestionConfig()

    def Initiate_Data_Ingestion(self):
        logging.info('Enter the data ingestion method or components')
        try:
            df = pd.read_csv('notebooks/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.Ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.Ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Train-Test split initiated.')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            logging.info('Train-Test split completed.')
            train_set.to_csv(self.Ingestion_config.train_data_path,index=False,header=True)
            logging.info(f'Train data saved to folder : {self.Ingestion_config.train_data_path}')
            test_set.to_csv(self.Ingestion_config.test_data_path,index=False,header=True)
            logging.info(f'Test data saved to folder : {self.Ingestion_config.test_data_path}')
            logging.info(f"Ingestion of data is completed!!")

            return (
                self.Ingestion_config.train_data_path,
                self.Ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.Initiate_Data_Ingestion()