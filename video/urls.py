from django.urls import path
from .views import get_video_list,get_video_detail


urlpatterns = [
    path('', get_video_list, name='video_list_url'),
    path('<str:slug>/', get_video_detail, name='video_detail_url')

]