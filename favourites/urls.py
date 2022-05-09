from django.urls import path
from . import views

app_name = 'favourites'
#
urlpatterns = [
#     path('', views.favourites_list, name='favor_detail'),
    path('add/<int:id>/', views.favourite_add, name='favor_add'),
#     # path('remove/<int:product_id>/', views.favor_remove, name='favor_remove'),
]