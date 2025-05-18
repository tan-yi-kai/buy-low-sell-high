from fastapi import APIRouter
import api.app.clients.FearGreed as FearGreed

router = APIRouter()

@router.get("/get_now")
async def get_now():
    return FearGreed.fetch_fear_greed()