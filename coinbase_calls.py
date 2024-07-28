from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
from dotenv import load_dotenv
import os
from json import dumps


## Extracting API key from .env secrets file for API calls
def load_api_key(key_name):
    load_dotenv()
    api_key = os.getenv(key_name)

    return api_key


client = EnhancedRESTClient(api_key=load_api_key('COINBASE_API_KEY'), api_secret=load_api_key("COINBASE_API_SECRET")) 
accounts = client.get_accounts()
print(dumps(accounts, indent=2))