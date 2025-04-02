import pandas as pd
from src.ds_e2e_project1.entity.config_entity import DataValidationConfig

class DataValidation:
  def __init__(self, data_val_config: DataValidationConfig):
    self.config = data_val_config

  def validate_columns(self) -> bool:
    try:
      data = pd.read_csv(self.config.unzip_data_dir)
      data_cols = list(data.columns)
      expected_cols =  self.config.expected_schema.keys()
      valid_status = None

      for data_col in data_cols:
        if data_col not in expected_cols:
          valid_status = False
          break
        else:
          valid_status = True
      
      with open(self.config.STATUS_FILE, "w") as f:
          f.write(f"Validation_status : {valid_status}")
      return valid_status
    except Exception as e:
      raise e
