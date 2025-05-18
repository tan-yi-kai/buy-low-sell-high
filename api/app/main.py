from fastapi import FastAPI
from api.app.routers import coingecko, fear_greed

#---------------------------------------------------------------------------------------------------
# Description: Main file for coordinating FAST API calls
# Run in Bash: uvicorn api.app.main:app --reload
# Visit http://127.0.0.1:8000/docs for API testing
#---------------------------------------------------------------------------------------------------


app = FastAPI(title = "Buy Low Sell High API")

app.include_router(fear_greed.router, prefix="/fear_greed", tags=["Fear & Greed"])
app.include_router(coingecko.router, prefix="/coingecko", tags=["CoinGecko Price Info"])

