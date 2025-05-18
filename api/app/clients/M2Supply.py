import pandas as pd
import datetime as datetime
from dotenv import load_dotenv
import os
from utils.api_utils import http_get_request

FRED_SERIES_ID_DICT = {
    "US": "M2SL",                   ## M2 Supply of United States
    "EUR": "MABMM201EZM189S",       ## M2 Supply of Europe
    "JPN": "JPNM2NSMABM",           ## M2 Supply of Japan
    "UK": "MABMM201GBM189S"         ## M2 Supply of United Kingdom
}


def fetch_country_m2(years=1, country_id="US"):
    url = "https://api.stlouisfed.org/fred/series/observations"
    
    load_dotenv()
    api_key = os.getenv("FRED_API_KEY")

    params = {
        "series_id": FRED_SERIES_ID_DICT[country_id],
        "api_key": api_key,
        "file_type": "json",
        "frequency": "m"
    }

    data = http_get_request(url=url, params=params)
    df = pd.DataFrame(data["observations"], columns=["date", "value"])
    df["date"] = pd.to_datetime(df["date"])

    return df



