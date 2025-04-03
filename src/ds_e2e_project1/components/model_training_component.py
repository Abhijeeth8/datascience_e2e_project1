from sklearn.linear_model import ElasticNet
import pandas as pd
import os
import joblib
from src.ds_e2e_project1.entity.config_entity import ModelTrainingConfig

class ModelTraining:
  def __init__(self, model_training_config: ModelTrainingConfig):
    self.config = model_training_config

  def load_train_test_data(self):
    train_data = pd.read_csv(self.config.train_data_path)
    X_train = train_data.drop(columns=[self.config.target_col])
    y_train = train_data[self.config.target_col]
    return X_train, y_train

  def train_ElasticNet_model(self):
    X_train, y_train = self.load_train_test_data()
    model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)

    model.fit(X=X_train, y=y_train)

    joblib.dump(model, filename=os.path.join(self.config.root_dir, self.config.model_name))