from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
  root_dir_for_data: Path
  source_url: str
  local_data_file: Path
  unzip_dir: Path

@dataclass
class DataValidationConfig:
  root_dir: Path
  unzip_data_dir: Path
  STATUS_FILE: Path
  expected_schema: dict

@dataclass
class DataTransformationConfig:
  root_dir: Path
  data_path: Path
  train_data_path: Path
  test_data_path: Path

@dataclass
class ModelTrainingConfig:
  root_dir: Path
  train_data_path: Path
  test_data_path: Path
  model_name: str
  alpha: float
  l1_ratio: float
  target_col: str

@dataclass
class ModelEvaluationConfig:
  root_dir: Path
  model_path: Path
  test_data_path: Path
  metrics_file_name: Path
  mlflow_tracking_uri: str
  target_col: str
  model_params: dict