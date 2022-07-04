from django.core.mail import send_mail
from decouple import config

DOMEIN = config("DOMEIN")

def send_activation_mail(user):
    message = f"""
Thank for registration.
Activate your account by sent email:
{DOMEIN}/account/activate/{user.activation_code}
"""
    send_mail(
        'Активация аккаунта',
        message,
        'shop@makers.com',
        [user.email, ]
    )