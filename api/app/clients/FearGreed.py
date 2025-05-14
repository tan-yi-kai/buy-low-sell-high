import requests
import pandas as pd

def fetch_fear_greed():
    url = "https://api.alternative.me/fng/?limit=1&format=json"
    response = requests.get(url).json()
    data = response["data"][0]

    return {
        "value": data["value"],
        "value_classification": data["value_classification"],
        "timestamp": pd.to_datetime(data["timestamp"], unit="s").isoformat()
    }
