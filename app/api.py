import requests
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from src.services.email import send_email


class GetValuesApi(APIView):
    def get(self, request: Request):
        """
        Returns the price of an asset and sends a value alert via e-mail
        """

        data = request.data
        asset_price = data.get("asset_price")
        symbol = data.get("symbol")
        url = f"{settings.ALPHA_VANTAGE}/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={settings.API_KEY}"
        response = requests.get(url=url)
        data = response.json()

        for value in data.values():
            price = value.get("05. price")

            if price > asset_price:
                return Response(
                    data={"active": symbol, "price": price, "message": "not buy"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            send_email(symbol=symbol, price=price)
            return Response(
                data={"active": symbol, "price": price, "message": "buy"},
                status=status.HTTP_200_OK,
            )
