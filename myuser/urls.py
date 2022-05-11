from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('activate/<str:activation_code>/', activate, name='activate'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('myprofile/<int:id>/', profile, name='profile'),

]