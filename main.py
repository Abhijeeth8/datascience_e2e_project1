from src.ds_e2e_project1 import logger
from src.ds_e2e_project1.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.ds_e2e_project1.pipeline.data_validation_pipeline import DataValidationPipeline


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


