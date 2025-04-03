import joblib
from pathlib import Path

class Predict:
  def __init__(self):
    self.model = joblib.load(Path("artifacts\model_training\wine_quality_estimator_model.joblib"))

  def predict(self, data):
    prediction = self.model.predict(data)
    return prediction