from flask_mail import Message, BadHeaderError
from shopproject import mail
from datetime import datetime

def send_email(recipient_email, email_body):
    try:
        msg = Message(
            subject="Reset Password Link",
            recipients = [recipient_email],
            body = email_body,
        )
        mail.send(msg)
    except BadHeaderError:
        return 1
    return 0

