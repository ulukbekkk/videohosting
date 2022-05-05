from django.urls import path
from .views import get_video_list


urlpatterns = [
    path('', get_video_list, name='video_list'),
]