from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('fertilizer_model.pkl')

with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

class FertilizerInput(BaseModel):
    Temperature: float
    Humidity: float
    Moisture: float
    Soil_Type: str
    Crop_Type: str
    Nitrogen: int
    Potassium: int
    Phosphorous: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fertilizer Recommendation API! Visit /docs to explore"}

@app.post("/recommend")
def recommend_fertilizer(input: FertilizerInput):
    soil_type_encoded = label_encoders['Soil_Type'].transform([input.Soil_Type])[0]
    crop_type_encoded = label_encoders['Crop_Type'].transform([input.Crop_Type])[0]
    
    features = np.array([[input.Temperature, input.Humidity, input.Moisture, soil_type_encoded,
                          crop_type_encoded, input.Nitrogen, input.Potassium, input.Phosphorous]])
    
    prediction = model.predict(features)
    fertilizer_name = label_encoders['Fertilizer'].inverse_transform(prediction)[0]
    
    return {"Recommended Fertilizer": fertilizer_name}
