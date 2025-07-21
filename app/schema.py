from pydantic import BaseModel

class DeliveryInput(BaseModel):
    DistanceKM: float
    Weather: str
    TimeOfDay: str
    
class PredictionResponse(BaseModel):
    Delayed: str