import os
import urllib.request as request
from src.ds_e2e_project1 import logger
import zipfile
from src.ds_e2e_project1.entity.config_entity import DataIngestionConfig
from src.ds_e2e_project1.utils.common import read_yaml, create_directories


class DataIngestion:
  def __init__(self, config:DataIngestionConfig):
    self.config = config
  
  def download_raw_data(self):
    if not os.path.exists(self.config.local_data_file):
      filename, headers = request.urlretrieve(url=self.config.source_url, filename=self.config.local_data_file)
      logger.info(f"{filename} downloaded from the url {self.config.source_url} with headers {headers}")
    else:
      logger.info(f"File already exists")

  def extract_zip_file(self):
    create_directories([self.config.unzip_dir])
    with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
      zip_ref.extractall(self.config.unzip_dir)