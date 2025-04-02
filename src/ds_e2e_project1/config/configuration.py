from src.ds_e2e_project1.constants import *
from src.ds_e2e_project1.utils.common import read_yaml, create_directories
from src.ds_e2e_project1.entity.config_entity import DataIngestionConfig

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
