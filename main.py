from src.ds_e2e_project1 import logger
from src.ds_e2e_project1.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME="Data Ingestion Stage"

if __name__ == "__main__":
  try:
    logger.info(f"--------stage {STAGE_NAME} started------------")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"--------stage {STAGE_NAME} completed------------")
  except Exception as e:
    raise e


