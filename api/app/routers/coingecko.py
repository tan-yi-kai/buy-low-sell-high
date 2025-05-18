from fastapi import APIRouter
import api.app.clients.CoinGecko as CoinGecko

router = APIRouter()

@router.get("/get_1_day")
async def get_1_day():
    return CoinGecko.fetch_btc_ohlc(days=1, fiat="usd")

