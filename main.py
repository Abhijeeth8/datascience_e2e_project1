from src.ds_e2e_project1 import logger
from src.ds_e2e_project1.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.ds_e2e_project1.pipeline.data_validation_pipeline import DataValidationPipeline
from src.ds_e2e_project1.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.ds_e2e_project1.pipeline.model_training_pipeline import ModelTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

if __name__ == "__main__":
  try:
    logger.info(f"--------stage {STAGE_NAME} started------------")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"--------stage {STAGE_NAME} completed------------")
  except Exception as e:
    raise e
  
  STAGE_NAME="Data Validation Stage"

  if __name__ == "__main__":
    try:
      logger.info(f"--------stage {STAGE_NAME} started------------")
      data_validation_pipeline = DataValidationPipeline()
      data_validation_pipeline.initiate_data_validation()
      logger.info(f"--------stage {STAGE_NAME} completed------------")
    except Exception as e:
      raise e
    
  STAGE_NAME="Data Transformation Stage"

  if __name__ == "__main__":
    try:
      logger.info(f"--------stage {STAGE_NAME} started------------")
      data_transformation_pipeline = DataTransformationPipeline()
      data_transformation_pipeline.initiate_data_transformation()
      logger.info(f"--------stage {STAGE_NAME} completed------------")
    except Exception as e:
      raise e
    

  STAGE_NAME="Model Training Stage"

  if __name__ == "__main__":
    try:
      logger.info(f"--------stage {STAGE_NAME} started------------")
      model_training_pipeline = ModelTrainingPipeline()
      model_training_pipeline.initiate_model_training()
      logger.info(f"--------stage {STAGE_NAME} completed------------")
    except Exception as e:
      raise e


