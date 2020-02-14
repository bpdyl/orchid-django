from django.core.mail import send_mail
from django.conf import settings
def sendmailtouser(subject=None,message=None,recipient_list=[]):
    try:
        send_mail(subject,message,from_email=settings.EMAIL_HOST,recipient_list=recipient_list)
        return True
    except:
        return False