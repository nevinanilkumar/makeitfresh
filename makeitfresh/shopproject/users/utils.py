from flask_mail import Message, BadHeaderError
from shopproject import mail
from datetime import datetime

def send_pwd_reset_email(recipient_email, url):
    try:
        msg = Message(
            subject="Reset Password Link",
            recipients = [recipient_email],
            body = 
                """To reset your password,  please click the following link.
                {}""".format(url)
        )
        mail.send(msg)
    except BadHeaderError:
        return 1
    return 0

def send_email_verif(recipient_email, url):
    try:
        msg = Message(
            subject="Email Verification",
            recipients = [recipient_email],
            body = 
                """Click the following linked to verify your email address.
                {}""".format(url)
        )
        mail.send(msg)
    except BadHeaderError:
        return 1
    return 0


