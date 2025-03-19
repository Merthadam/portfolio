import smtplib as smtp
import ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "merthadam9@gmail.com"
    password = "evpykczgbiastrzb"
    receiver = "merthadam9@gmail.com"

    context = ssl.create_default_context()

    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
