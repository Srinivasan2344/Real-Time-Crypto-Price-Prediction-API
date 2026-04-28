from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class CryptoInput(BaseModel):
    coin_name:str
    open_price:float = Field(...,gt=0)
    close_price:float = Field(...,gt=0)
    high_price:float = Field(...,gt=0)
    low_price:float = Field(...,gt=0)
    volume:float = Field(...,gt=0)


@app.get("/")
def home():
    return {"message":"API Working"}


@app.post("/predict")
def predict(data: CryptoInput):

    try:

        if data.low_price > data.high_price:
            raise HTTPException(
                status_code=400,
                detail="Invalid price input"
            )

        if data.close_price > data.open_price:
            trend="Bullish"
        else:
            trend="Bearish"

        return {
            "prediction":trend,
            "confidence_score":0.72,
            "volatility_level":"Medium"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/market-insight")
def market_insight():
    return {
        "Coin":"Bitcoin",
        "Trend":"Bullish",
        "Volatility":"Medium",
        "Volume Trend":"Increasing"
    }