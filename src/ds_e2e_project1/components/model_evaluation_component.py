import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import accuracy_score, r2_score, confusion_matrix, classification_report, mean_squared_error, mean_absolute_error
import mlflow
from mlflow.models import infer_signature 
import mlflow.sklearn
import os
from urllib.parse import urlparse
import numpy as np
from src.ds_e2e_project1.utils.common import save_json_data
from src.ds_e2e_project1.entity.config_entity import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
  def __init__(self, model_eval_config: ModelEvaluationConfig):
    self.config = model_eval_config

  def get_model(self):
    model = joblib.load(self.config.model_path)
    return model
  
  def get_test_data(self):
    test_data = pd.read_csv(self.config.test_data_path)
    X_test = test_data.drop(columns=[self.config.target_col])
    y_test = test_data[self.config.target_col]
    return X_test, y_test
  
  def get_evaluation_results(self):
    X_test, y_test = self.get_test_data()
    model = self.get_model()

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = (mean_squared_error(y_test, y_pred))**(1/2)
    model_scores = {"r2":r2, "mae":mae, "rmse":rmse}

    save_json_data(dest_json_file_path =  Path(self.config.metrics_file_name), json_data=model_scores)


    return model_scores

  def log_to_mlflow(self):
    model = model = self.get_model()
    model_scores = self.get_evaluation_results()

    X_test, y_test = self.get_test_data()

    mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
    mlflow.set_experiment("Wine_quality_estimator_ds1")

    with mlflow.start_run():
      # infer_signature(X_test, y_test)


      mlflow.log_params(self.config.model_params)
      mlflow.log_metrics(model_scores)

      tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

      if tracking_url_type_store != "file":
        mlflow.sklearn.log_model(model, "model", registered_model_name="Wine_quality_predictor_elasticnet")
      else:
        mlflow.sklearn.log_model(model, "model")
