from src.ds_e2e_project1.config.configuration import ConfigurationManager
from src.ds_e2e_project1.components.data_transformation_component import DataTransformation

class DataTransformationPipeline:
  def __init__(self):
    pass

  def initiate_data_transformation(self):
    config_manager = ConfigurationManager()
    data_transformation_config = config_manager.get_data_transformation_configuration()
    data_transformation = DataTransformation(data_transformation_config)
    data_transformation.transform_data_tt_split()