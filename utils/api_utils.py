import requests
from typing import Dict

## HTTP GET request handler
def http_get_request(url: str, params: Dict = None, headers: Dict = None, timeout: int = 15):
    try: 
        response = requests.get(url=url, params=params, headers=headers, timeout=timeout)
        status = response.status_code

        return response.json()
    
    except requests.RequestException as e:
        print(f"GET Request has failed: {e}")
        
        return None
