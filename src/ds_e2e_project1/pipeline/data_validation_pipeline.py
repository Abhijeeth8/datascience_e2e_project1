from src.ds_e2e_project1.config.configuration import ConfigurationManager
from src.ds_e2e_project1.components.data_validation_component import DataValidation
from src.ds_e2e_project1 import logger

class DataValidationPipeline:
  def __init__(self):
    pass

  def initiate_data_validation(self):
    config_manager = ConfigurationManager()
    validation_config = config_manager.get_data_validation_config()
    data_validation = DataValidation(validation_config)
    is_data_valid = data_validation.validate_columns()
    logger.info(f"Is the data valid : {is_data_valid}")
