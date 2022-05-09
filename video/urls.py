from django.urls import path
from .views import *

# app_name = 'video'

urlpatterns = [
    path('', get_video_list, name='video_list_url'),
    # path('base/nezahodit/', get_base_html, name='basika'),
    path('search_video/', search_video, name='search_url'),
    path('create_video/', create_video, name='create_video_url'),
    path('delete_comment/<int:id>/', delete_comment, name='delete_comment_url'),
    path('delete_video/<int:pk>', detele_video, name='delete_video_url'),
    path('update_video/<int:id>', update_video, name='update_video_url'),
    path('video/<str:slug>/', get_video_detail, name='video_detail_url'),
    path('fav/<str:slug>/', fav, name='fav_url'),
    path('fav/', get_fav, name='get_fav_url'),
    path('<str:category_slug>/', get_video_list, name='video_list_by_category'),



]