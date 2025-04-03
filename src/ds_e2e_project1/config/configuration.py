import os
from src.ds_e2e_project1.constants import *
from src.ds_e2e_project1.utils.common import read_yaml, create_directories
from src.ds_e2e_project1.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig

class ConfigurationManager:
  def __init__(
    self,
    config_file_path=CONFIG_FILE_PATH,
    params_file_path=PARAMS_FILE_PATH,
    schema_file_path=SCHEMA_FILE_PATH):
    self.config=read_yaml(config_file_path)
    self.params=read_yaml(params_file_path)
    self.schema=read_yaml(schema_file_path)

    create_directories([self.config.artifacts_root])

  def get_data_ingestion_config(self) -> DataIngestionConfig:
    create_directories([self.config.data_ingestion.root_dir_for_data])
    
    dataIngestionConfig = DataIngestionConfig(
      root_dir_for_data=self.config.data_ingestion.root_dir_for_data,
      source_url=self.config.data_ingestion.source_url,
      local_data_file=self.config.data_ingestion.local_data_file,
      unzip_dir=self.config.data_ingestion.unzip_dir
    )
    return dataIngestionConfig
  
  def get_data_validation_config(self) -> DataValidationConfig:
    config = self.config.data_validation
    create_directories([config.root_dir])

    dataValidationConfig = DataValidationConfig(
      unzip_data_dir= config.unzip_data_dir,
      root_dir= config.root_dir,
      STATUS_FILE= config.STATUS_FILE,
      expected_schema= self.schema.COLUMNS
    )
    return dataValidationConfig
  
  def get_data_transformation_configuration(self) -> DataTransformationConfig:
    config = self.config.data_transformation
    create_directories([config.root_dir])


    data_transformation_config = DataTransformationConfig(
      data_path= config.data_path,
      root_dir=config.root_dir,
      train_data_path = os.path.join(config.root_dir, "train.csv"),
      test_data_path = os.path.join(config.root_dir, "test.csv")
    )

    return data_transformation_config
  
  def get_model_training_config(self) -> ModelTrainingConfig:
    config = self.config.model_training
    create_directories([config.root_dir])

    model_training_config = ModelTrainingConfig(
      alpha=self.params.ElasticNet.alpha,
      l1_ratio=self.params.ElasticNet.l1_ratio,
      target_col=self.schema.TARGET_COLUMN.name,
      model_name=config.model_name,
      root_dir=config.root_dir,
      test_data_path=config.test_data_path,
      train_data_path=config.train_data_path
    )
    
    return model_training_config

