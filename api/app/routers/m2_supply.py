from fastapi import APIRouter
from api.app.clients.M2Supply import fetch_country_m2

router = APIRouter()

@router.get("/get_country")
async def get_country(country_id="US", years=3):
    return fetch_country_m2(country_id=country_id, years=years)
