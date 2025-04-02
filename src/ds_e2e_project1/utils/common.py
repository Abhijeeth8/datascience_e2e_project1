import os
import yaml
import json
import joblib
from src.ds_e2e_project1 import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from box.exceptions import BoxValueError
from typing import Any

@ensure_annotations
def read_yaml(yaml_file_path: Path) -> ConfigBox:
  try:
    with open(yaml_file_path, "r") as yaml_file:
      yaml_content = yaml.safe_load(yaml_file)
      logger.info(f"YAML file {yaml_file_path} read successfully")
      return ConfigBox(yaml_content)
  except BoxValueError:
    raise ValueError("YAML file empty")
  except Exception as e:
    raise e
  
@ensure_annotations
def create_directories(dirs_paths: list, verbose=True):
  for dir_path in dirs_paths:
    os.makedirs(dir_path, exist_ok=True)
    if verbose:
      logger.info(f"Directory {dir_path} created")

@ensure_annotations
def save_json_data(dest_json_file_path: Path, json_data: dict):
  with open(dest_json_file_path,"w") as json_file:
    json.dump(json_data, json_file, indent=4)

  logger.info(f"Given json data saved to file {dest_json_file_path}")

@ensure_annotations
def load_json_data(source_json_file_path: Path, json_data: dict) -> ConfigBox:
  with open(source_json_file_path,"r") as json_file:
    json_data = json.load(json_file)

  logger.info(f"Data loaded from file {source_json_file_path}")
  return ConfigBox(json_data)

@ensure_annotations
def save_binaries(binary_data: Any, dest_bin_file_path: Path):
  joblib.dump(value=binary_data, filename=dest_bin_file_path)
  logger.info(f"Given bin data saved to file {dest_bin_file_path}")

@ensure_annotations
def load_binaries(source_bin_file_path: Path) -> Any:
  bin_data = joblib.load(filename=source_bin_file_path)
  logger.info(f"Binary data loaded from file {source_bin_file_path}")
  return bin_data
