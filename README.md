🌸 Iris Species Prediction API 🌸
This repository contains a FastAPI-based machine learning API for predicting Iris flower species. The model is trained on the Iris dataset and is deployed as a web service using FastAPI.

🚀 Features
1. FastAPI Backend for quick and efficient API calls.
2. Pretrained Machine Learning Model using iris_model.pkl.
3. POST Endpoint to predict species based on four input features:
Sepal Length
Sepal Width
Petal Length
Petal Width

🔧 Setup & Installation
Clone this repository:
git clone https://github.com/yourusername/iris-prediction-api.git


Navigate to the project folder:
cd iris-prediction-api


Install dependencies:
pip install -r requirements.txt

Run the API:
uvicorn app:app --host 0.0.0.0 --port 8000


📡 API Endpoints
GET / - Returns a welcome message.
POST /predict - Accepts JSON input and returns the predicted species.
Example Request:
json
CopyEdit
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Example Response:
json
CopyEdit
{
  "predicted_species": "Iris-setosa"
}

📜 License
This project is open-source and available under the MIT License.

