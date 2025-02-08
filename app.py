from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("iris_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Welcome to the Iris Species Prediction API"}

@app.post("/predict")
def predict_species(data: IrisInput):
    # Convert input to model format
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    return {"predicted_species": prediction}
