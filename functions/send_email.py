import os, smtplib, ssl

host = 'smtp.gmail.com'
port = 465
username = 'developmentandrzejr@gmail.com'
password = os.environ['PMCGooglePass']
context = ssl.create_default_context()
receiver = 'developmentandrzejr@gmail.com'

message = """Subject: Hello from Python!
Hello! This is an email sent from Python.
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
