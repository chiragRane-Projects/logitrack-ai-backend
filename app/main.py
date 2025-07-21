from fastapi import FastAPI
from app.model import load_model_encoders, predict_delay
from app.schema import DeliveryInput, PredictionResponse

app = FastAPI(title="Logistics ML Backend")

model, encoders = load_model_encoders()

@app.get("/")
def health_check():
    return {"message": "Backend is live"}

@app.post("/predict-delay")
def predict(data: DeliveryInput):
    result = predict_delay(data, model, encoders)
    return {"Delayed": result}