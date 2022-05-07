from django.urls import path
from .views import get_video_list,get_video_detail, create_video, update_video, detele_video, search_video

# app_name = 'video'

urlpatterns = [
    path('', get_video_list, name='video_list_url'),
    path('search_video/', search_video, name='search_url'),
    path('create_video/', create_video, name='create_video_url'),
    path('delete_video/<int:pk>', detele_video, name='delete_video_url'),
    path('update_video/<int:id>', update_video, name='update_video_url'),
    path('<str:slug>/', get_video_detail, name='video_detail_url')

]