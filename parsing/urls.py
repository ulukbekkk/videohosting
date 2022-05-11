from django.urls import path

from .views import get_parser

urlpatterns = [
    path('  ', get_parser, name='parsing_url')
]