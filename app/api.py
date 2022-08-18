import email.message
import smtplib

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings


class GetValuesApi(APIView):
    def get(self, request):
        """
        Returns the price of an asset and sends a value alert via e-mail
        """

        asset_price = "33.0"
        symbol = "PETR4.SA"
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

            self._send_email(symbol=symbol, price=price)
            return Response(
                data={"active": symbol, "price": price, "message": "buy"},
                status=status.HTTP_200_OK,
            )

    def _send_email(self, symbol: str, price: str):
        body = f"""
        <p>Olá, Investidor!</p>
        <p>A cotação do seu ativo chegou ao valor estabelecido! E ai, bora comprar?</p>
        <p>Ativo: {symbol}, Valor: R$ {price}</p>
        <p>E-mail enviado automaticamente.</p>
        """

        """
        Initial settings for sending the e-mail
        """
        msg = email.message.Message()
        msg["Subject"] = "Cotação Diária de Ativos"
        msg["From"] = settings.EMAIL
        msg["To"] = settings.EMAIL
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(payload=body)

        """
        Login Credentials for sending the e-mail
        """
        send_email = smtplib.SMTP("smtp.gmail.com: 587")
        send_email.starttls()
        send_email.login(msg["From"], settings.PASSWORD)
        send_email.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
