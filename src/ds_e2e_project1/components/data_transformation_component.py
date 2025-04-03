import pandas as pd
from sklearn.model_selection import train_test_split
from src.ds_e2e_project1 import logger
from src.ds_e2e_project1.entity.config_entity import DataTransformationConfig

class DataTransformation:
  def __init__(self, data_transformation_config: DataTransformationConfig):
    self.config = data_transformation_config

  def transform_data_tt_split(self):
    data = pd.read_csv(self.config.data_path)
    train, test = train_test_split(data, test_size=0.20, random_state=42)


    train.to_csv(self.config.train_data_path, index=False)
    test.to_csv(self.config.test_data_path, index=False)


    logger.info(f"Data split into train and test datasets with shapes:\nTrain data shape : {train.shape}\nTest data shape : {test.shape}")
