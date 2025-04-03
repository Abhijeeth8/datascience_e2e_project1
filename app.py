from flask import Flask, request
import os
from src.ds_e2e_project1.pipeline.prediction_pipeline import Predict
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_for_data():
  try:
    fixed_acidity =float(request.form['fixed_acidity'])
    volatile_acidity =float(request.form['volatile_acidity'])
    citric_acid =float(request.form['citric_acid'])
    residual_sugar =float(request.form['residual_sugar'])
    chlorides =float(request.form['chlorides'])
    free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
    total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
    density =float(request.form['density'])
    pH =float(request.form['pH'])
    sulphates =float(request.form['sulphates'])
    alcohol =float(request.form['alcohol'])
  

  
    data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
    data = np.array(data).reshape(1, 11)
    print(data)
    prediction_pipeline = Predict()
    prediction = prediction_pipeline.predict(data)
    print("done")
    return str(prediction)
  except Exception as e:
    raise "Something went wrong"
  # return "Hello"

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5001)