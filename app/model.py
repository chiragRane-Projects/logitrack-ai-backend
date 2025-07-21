import joblib

def load_model_encoders():
    model = joblib.load("model.pkl")
    encoders = joblib.load("encoders.pkl")
    return model, encoders

def predict_delay(data, model, encoders):
    weather_encoded = encoders["Weather"].transform([data.Weather])[0]
    time_encoded = encoders["TimeOfDay"].transform([data.TimeOfDay])[0]
    
    X = [[data.DistanceKM, weather_encoded, time_encoded]]
    
    prediction = model.predict(X)[0]
    
    predicted_label = encoders["Delayed"].inverse_transform([prediction])[0]
    return predicted_label