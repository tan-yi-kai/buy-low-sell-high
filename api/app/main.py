from fastapi import FastAPI
from api.app.routers import fear_greed

#---------------------------------------------------------------------------------------------------
# Description: Main file for coordinating FAST API calls
# Visit http://127.0.0.1:8000/docs for API testing
#---------------------------------------------------------------------------------------------------


app = FastAPI(title = "Buy Low Sell High API")

app.include_router(fear_greed.router, prefix="/indicators", tags=["Indicators"])
