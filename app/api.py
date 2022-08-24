from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.services.alpha_vantage import ServiceAlphaVantageAPI
from src.services.email import ServiceSendEmail


class GetValuesApi(APIView):

    service_alpha = ServiceAlphaVantageAPI()
    service_email = ServiceSendEmail()

    def post(self, request: Request):
        req = request.data
        asset_price = req.get("asset_price")
        symbol = req.get("symbol")

        data = self.service_alpha.get_values(symbol=symbol)

        if data >= asset_price:
            self.service_email.send_email_sell(symbol=symbol, price=data)
            return Response(
                data={"active": symbol, "price": data, "message": "sell"},
                status=status.HTTP_200_OK,
            )
        else:
            self.service_email.send_email_buy(symbol=symbol, price=data)
            return Response(
                data={"active": symbol, "price": data, "message": "buy"},
                status=status.HTTP_200_OK,
            )
