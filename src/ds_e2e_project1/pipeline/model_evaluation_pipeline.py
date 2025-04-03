from src.ds_e2e_project1.config.configuration import ConfigurationManager
from src.ds_e2e_project1.components.model_evaluation_component import ModelEvaluation

class ModelEvaluationPipeline:
  def __init__(self):
    pass

  def initiate_model_evaluation(self):
    config_manager = ConfigurationManager()
    model_eval_config = config_manager.get_model_eval_config()
    model_eval = ModelEvaluation(model_eval_config)
    model_eval.log_to_mlflow()