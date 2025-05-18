import requests
import pandas as pd
import datetime as datetime 
from dotenv import load_dotenv
import os

def fetch_btc_ohlc(days=1, fiat="usd"):
    url = r"https://api.coingecko.com/api/v3/coins/bitcoin/ohlc"
    
    load_dotenv()
    coingecko_api_key = os.getenv("COINGECKO_API_KEY")
    
    headers = {
        "x-cg-demo-api-key": coingecko_api_key
    }
    
    params = {
        "vs_currency": fiat,
        "days": days
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(f"fetch_btc_ohlc() failed, {response.status_code}: {response.text}")
    
    ohlc_data = response.json()
    df = pd.DataFrame(ohlc_data, columns=["timestamp_ms", "open", "high", "low", "close"])
    df["timestamp"] = pd.to_datetime(df["timestamp_ms"], unit="ms")
    df.drop(columns=["timestamp_ms"], inplace=True)

    return df

