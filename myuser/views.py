from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from video.models import Fav
from .forms import RegistrationForm
from django.shortcuts import get_object_or_404, redirect, render

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = 'https://mail.google.com/'
    success_message = 'Successfully registered'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form(self.get_form_class())
        return context


class SignInView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.get_form(self.get_form_class())
        return context


def profile(request, id):
    user = User.objects.get(id=request.user.id)
    fav = Fav.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'fav': fav})


def activate(request, activation_code):
    # print('asdasdasdasd')
    user = get_object_or_404(User, activation_code=activation_code)
    # print(user, 'asdasdasdasdasd')
    user.is_active = True
    user.activation_code = ''
    user.save()
    return redirect(reverse_lazy('login'))


