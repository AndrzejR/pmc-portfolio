import os, smtplib, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'developmentandrzejr@gmail.com'
    password = os.environ['PMCGooglePass']
    context = ssl.create_default_context()
    receiver = 'developmentandrzejr@gmail.com'

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    message = """Subject: Test Hello from send_email
    send_email was run as __main__
    """
    send_email(message)