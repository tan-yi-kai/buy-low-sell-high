from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
from dotenv import load_dotenv
import os
from json import dumps


## Extracting API key from .env secrets file for API calls
def load_api_key(key_name):
    load_dotenv()
    api_key = os.getenv(key_name)

    return api_key


## Setting up client with authentication
client = EnhancedRESTClient(api_key=load_api_key('COINBASE_API_KEY'), api_secret=load_api_key("COINBASE_API_SECRET")) 

## API call to get candle information using UNIX timestamps
accounts = client.get_public_candles(product_id="BTC-USD", start="1721750400", end="1722355200", granularity="ONE_DAY")

## Printing out information retrieved from API call
print(dumps(accounts, indent=2))