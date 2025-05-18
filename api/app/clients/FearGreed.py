import pandas as pd
from utils.api_utils import http_get_request

def fetch_fear_greed():
    url = "https://api.alternative.me/fng/?limit=1&format=json"
    
    response = http_get_request(url=url)
    
    data = response["data"][0]

    return {
        "value": data["value"],
        "value_classification": data["value_classification"],
        "timestamp": pd.to_datetime(data["timestamp"], unit="s").isoformat()
    }
