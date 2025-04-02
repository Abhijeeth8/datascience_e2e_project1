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