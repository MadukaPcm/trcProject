from datetime import datetime
from pytz import utc
from django.shortcuts import HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail

def MyFunc():
    try:
        subject = 'Your accounts needs to be verified'
        message = f'Hi bro frank'
        # message = f'Hi verify your account 127.0.0.1:8000/verify/{token}' #for localhost use.
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['madukapcm@gmail.com',]
        send_mail(subject, message,email_from,recipient_list)
    except Exception as e:
        print(e)
        
    return HttpResponse(status=204)
    
    
def MyFuncView():
    try:
        subject = 'Your accounts needs to be verified'
        message = f'Nakubalii maduka'
        # message = f'Hi verify your account 127.0.0.1:8000/verify/{token}' #for localhost use.
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['madukapcm@gmail.com',]
        send_mail(subject, message,email_from,recipient_list)
    except Exception as e:
        print(e)
        
    return HttpResponse(status=204)