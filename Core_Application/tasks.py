from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import volunteer
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
import time

logger = get_task_logger(__name__)

@shared_task(bind=True, max_retries=3, rate_limit='10/m')
def save_volunteer_data(self, name, email, msg, time, date):
    """
    Save volunteer data asynchronously
    Rate limited to 10 saves per minute
    """
    try:
        volunteer_data = volunteer(
            name=name,
            email=email,
            msg=msg,
            time=time,
            date=date
        )
        volunteer_data.save()
        logger.info(f"Saved volunteer data for {email}")
        return True
    except Exception as exc:
        logger.error(f"Error saving volunteer data: {exc}")
        self.retry(exc=exc, countdown=5)  # Retry after 5 seconds
        return False

@shared_task(bind=True, max_retries=3, rate_limit='30/m')
def send_thank_you_email(self, name, email, date, formatted_time):
    """
    Send thank you email asynchronously
    Rate limited to 30 emails per minute
    """
    try:
        message_id = f"<{int(time.time())}@humblehandfoundation.com>"
        
        subject = f"HumbleHandFoundation - {date}"
        message = (
            f"Dear {name},\n\n"
            "Thank you for reaching out to HumbleHandFoundation. We have received your message.\n\n"
            f"This is an automated confirmation sent on {date} at {formatted_time}.\n\n"
            "About HumbleHandFoundation:\n"
            "We are dedicated to making a positive impact in our community through various initiatives "
            "and volunteer programs. Your interest in our organization means a lot to us.\n\n"
            "Stay Connected:\n"
            "- Follow us on social media\n"
            "- Visit our website for updates\n"
            "- Join our newsletter\n\n"
            "Best regards,\n"
            "HumbleHandFoundation Team\n"
            f"\nReference ID: MSG-{date.replace('/', '')}-{formatted_time.replace(':', '').replace(' ', '')}"
        )

        logger.info(f"Attempting to send email to {email}")
        logger.info(f"Using email settings: HOST={settings.EMAIL_HOST}, PORT={settings.EMAIL_PORT}")
        
        try:
            # First try with simple send_mail
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            logger.info(f"Successfully sent email using send_mail to {email}")
            return True
        except Exception as simple_mail_error:
            logger.error(f"Simple mail failed: {str(simple_mail_error)}")
            
            # Try with EmailMessage if send_mail fails
            try:
                email_message = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[email],
                    headers={
                        'Message-ID': message_id,
                        'In-Reply-To': '',
                        'References': '',
                        'Thread-Index': message_id,
                    }
                )
                
                email_message.send(fail_silently=False)
                logger.info(f"Successfully sent email using EmailMessage to {email}")
                return True
            except Exception as email_message_error:
                logger.error(f"EmailMessage failed: {str(email_message_error)}")
                raise  # Re-raise the exception for retry

    except Exception as exc:
        logger.error(f"Error sending email: {exc}")
        logger.error(f"Email settings used: HOST_USER={settings.EMAIL_HOST_USER}")
        self.retry(exc=exc, countdown=10)
        return False 