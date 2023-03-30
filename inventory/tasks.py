from django.core.mail import send_mail
from django.conf import settings

def send_reminder_email():
    try:
        subject = 'Your accounts needs to be verified'
        message = f'Hi bro frank'
        # message = f'Hi verify your account 127.0.0.1:8000/verify/{token}' #for localhost use.
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['madukapcm@gmail.com',]
        send_mail(subject, message,email_from,recipient_list)
    except Exception as e:
        print(e)
        
    # return HttpResponse(status=204)




# from datetime import date
# from django.core.mail import send_mail
# from django.conf import settings
# from myapp.models import Asset

# def send_reminder_email():
#     # Get all assets that are due for maintenance today
#     assets_due = Asset.objects.filter(maintenance_date=date.today())

#     # Send an email to the technician for each asset due
#     for asset in assets_due:
#         subject = f'Reminder: Asset {asset.name} due for maintenance'
#         message = f'Asset {asset.name} is due for maintenance today. Please attend to it.'
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_FROM,
#             [asset.technician.email],
#             fail_silently=False,
#         )