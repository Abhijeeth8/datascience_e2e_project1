from src.ds_e2e_project1.entity.config_entity import DataIngestionConfig
from src.ds_e2e_project1.config.configuration import ConfigurationManager
from src.ds_e2e_project1.components.data_ingestion_component import DataIngestion
from src.ds_e2e_project1 import logger

class DataIngestionPipeline:
  def __init__(self):
    pass

  def initiate_data_ingestion(self):
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_raw_data()
    data_ingestion.extract_zip_file()
    



