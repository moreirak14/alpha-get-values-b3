import email.message
import smtplib

from config import settings


def send_email_buy(symbol: str, price: str):
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
    config_email = smtplib.SMTP("smtp.gmail.com: 587")
    config_email.starttls()
    config_email.login(msg["From"], settings.PASSWORD)
    config_email.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))


def send_email_sell(symbol: str, price: str):
    body = f"""
    <p>Olá, Investidor!</p>
    <p>A cotação do seu ativo valorizou! E ai, bora vender?</p>
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
    config_email = smtplib.SMTP("smtp.gmail.com: 587")
    config_email.starttls()
    config_email.login(msg["From"], settings.PASSWORD)
    config_email.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
