from PriceScraper import *



if __name__ == "__main__":
    
    api_key = load_scraper_api_key()    
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/BTC?from=2023-08-10&to=2023-09-10&apikey={api_key}"
    json = call_url(url) 
    print(json)