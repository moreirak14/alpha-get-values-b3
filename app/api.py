import requests
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from src.services.email import send_email_buy, send_email_sell


class GetValuesApi(APIView):
    def get(self, request: Request):
        """
        Returns the price of an asset and sends a value alert via e-mail
        """

        data_input = request.data
        asset_price = data_input.get("asset_price")
        symbol = data_input.get("symbol")
        url = f"{settings.ALPHA_VANTAGE}/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={settings.API_KEY}"
        response = requests.get(url=url)
        data_output = response.json()

        for value in data_output.values():
            price = value.get("05. price")

            if price >= asset_price:
                send_email_sell(symbol=symbol, price=price)
                return Response(
                    data={"active": symbol, "price": price, "message": "sell"},
                    status=status.HTTP_200_OK,
                )
            else:
                send_email_buy(symbol=symbol, price=price)
                return Response(
                    data={"active": symbol, "price": price, "message": "buy"},
                    status=status.HTTP_200_OK,
                )
