import pandas as pd
import datetime as datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import os
from utils.api_utils import http_get_request


FRED_SERIES_ID_DICT = {
    "US": "M2SL",                   ## M2 Supply of United States
    "EUR": "MABMM201EZM189S",       ## M2 Supply of Europe
    "JPN": "JPNM2NSMABM",           ## M2 Supply of Japan
    "UK": "MABMM201GBM189S"         ## M2 Supply of United Kingdom
}


def generate_params(country_id: str, years: int, file_type: str = "json", frequency: str = "m") -> dict[str: str]:
    
    load_dotenv()
    api_key = os.getenv("FRED_API_KEY")

    end_date = datetime.date.today()
    start_date = end_date - relativedelta(years=int(3))

    params = {
        "series_id": FRED_SERIES_ID_DICT[country_id],
        "api_key": api_key,
        "file_type": "json",
        "frequency": "m",
        "observation_start": start_date.strftime("%Y-%m-%d"),
        "observation_end": end_date.strftime("%Y-%m-%d")
    }

    return params


def fetch_country_m2(years: int=3, country_id: str="US"):
    url = "https://api.stlouisfed.org/fred/series/observations"

    params = generate_params(country_id, years)
    
    data = http_get_request(url, params)
    df = pd.DataFrame(data["observations"], columns=["date", "value"])
    df["date"] = pd.to_datetime(df["date"])

    return df


def fetch_global_m2(years: int = 1, country_id: list = ["US", "EUR", "JPN", "UK"]):
    url = "https://api.stlouisfed.org/fred/series/observations"
    
    load_dotenv()
    api_key = os.getenv("FRED_API_KEY")
    
    pass

