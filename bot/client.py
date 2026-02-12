import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv() # Loads variables from .env

class BinanceTestnetClient:
    def __init__(self, api_key=None, api_secret=None):
        # Use provided keys, otherwise fallback to .env file
        self.api_key = api_key or os.getenv('BINANCE_API_KEY')
        self.api_secret = api_secret or os.getenv('BINANCE_API_SECRET')
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API Key and Secret must be provided in .env or UI")
            
        self.client = Client(self.api_key, self.api_secret, testnet=True)