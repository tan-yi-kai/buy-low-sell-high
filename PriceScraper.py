import requests

from dotenv import load_dotenv
import os



######## Uses Fiancial Modeling Prep API calls to scrape historical stock data
######## More info can be found at https://site.financialmodelingprep.com



## Extracting API key from .env secrets file for API calls
def load_scraper_api_key():
    load_dotenv()
    api_key = os.getenv("SCRAPER_API_KEY")
    
    return api_key


## TODO
## Returns appropriate API call based on user's requirement
def command_builder(url):
    return


## Uses request library to execute HTTP requests for API
def call_url(url):
    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None
    


