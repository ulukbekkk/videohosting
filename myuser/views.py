from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from video.models import Video, Fav
from .models import User
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('video_list_url')
    success_message = 'Successfully registered'


class SignInView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('video_list_url')


def profile(request, id):
    user = User.objects.get(id=request.user.id)
    fav = Fav.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'fav': fav})


