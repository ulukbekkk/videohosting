from django.core.mail import send_mail


def send_activation_mail(user):
    message = f"""
Thank for registration.
Activate your account by sent email:
http://127.0.0.1:8000/account/activate/{user.activation_code}
"""
    send_mail(
        'Активация аккаунта',
        message,
        'shop@makers.com',
        [user.email, ]
    )