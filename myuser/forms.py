from django.forms import ModelForm, CharField, PasswordInput, ValidationError
from django.contrib.auth import get_user_model
from .heplers import send_activation_mail

User = get_user_model()


class RegistrationForm(ModelForm):
    password = CharField(min_length=8, max_length=20, required=True, widget=PasswordInput)
    password_confirmation = CharField(min_length=8, max_length=20, required=True, widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',
                  'first_name', 'last_name', 'image')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('User with given username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('User with given email already exists')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise ValidationError('Passwords do not match')
        return data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        send_activation_mail(user)
        return user

