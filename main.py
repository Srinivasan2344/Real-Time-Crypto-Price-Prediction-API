from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CryptoInput(BaseModel):
    coin_name:str
    open_price:float
    close_price:float
    high_price:float
    low_price:float
    volume:float

@app.get("/")
def home():
    return {"message":"API Working"}

@app.post("/predict")
def predict(data: CryptoInput):
    return {
        "prediction":"Bullish",
        "confidence_score":0.72,
        "volatility_level":"Medium"
    }

@app.get("/market-insight")
def market():
    return {
        "Coin":"Bitcoin",
        "Trend":"Bullish",
        "Volatility":"Medium",
        "Volume Trend":"Increasing"
    }