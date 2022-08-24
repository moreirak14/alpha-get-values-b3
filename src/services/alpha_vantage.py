import requests

from config import settings
from src.exception import PageNotLoaded


class ServiceAlphaVantageAPI:
    def get_values(self, symbol: str):
        """
        Returns the price of an asset
        """

        url = f"{settings.ALPHA_VANTAGE}/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={settings.API_KEY}"
        response = requests.get(url=url)

        if response.status_code != 200:
            raise PageNotLoaded

        obj = response.json()

        for value in obj.values():
            return value.get("05. price")
