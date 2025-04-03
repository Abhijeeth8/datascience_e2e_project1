from src.ds_e2e_project1.config.configuration import ConfigurationManager
from src.ds_e2e_project1.components.model_training_component import ModelTraining

class ModelTrainingPipeline:
  def __init__(self):
    pass
  
  def initiate_model_training(self):
    config_manager = ConfigurationManager()
    model_training_config = config_manager.get_model_training_config()
    model_training = ModelTraining(model_training_config)
    model_training.train_ElasticNet_model()