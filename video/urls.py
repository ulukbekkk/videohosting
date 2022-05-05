from django.urls import path
from .views import get_video_list,get_video_detail, create_video

app_name= 'video'

urlpatterns = [
    path('', get_video_list, name='video_list_url'),
    path('create_video/', create_video, name='create_video'),
    path('<str:slug>/', get_video_detail, name='video_detail_url')

]