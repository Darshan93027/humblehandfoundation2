from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client(recipient_email):
    subject = "Send Mail"
    message = "This is a sample email sent using Django."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [recipient_email]
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email: {e}"
