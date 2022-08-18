from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from config import settings
import requests


class GetValuesApi(APIView):

    def get(self, request):
        """
        Return the price of an asset
        """

        asset_price = "32.0"
        symbol = "PETR4.SA"
        url = f"{settings.ALPHA_VANTAGE}/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={settings.API_KEY}"
        response = requests.get(url=url)
        data = response.json()

        for value in data.values():
            price = value.get("05. price")
            # print(f"Preço atual: {price}")
            # print(f"Preço que desejo comprar: {asset_price}")

            if price <= asset_price:
                return Response(data={
                    "active": symbol,
                    "price": price,
                    "message": "buy"
                }, status=status.HTTP_200_OK)
            else:
                return Response(data={
                    "active": symbol,
                    "price": price,
                    "message": "not buy"
                }, status=status.HTTP_400_BAD_REQUEST)
