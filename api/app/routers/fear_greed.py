from fastapi import APIRouter
import api.app.clients.FearGreed as FearGreed

router = APIRouter()

@router.get("/fear_greed")
async def get_fear_greed():
    return FearGreed.fetch_fear_greed()