from django.shortcuts import render
from .parsings import zipped

def get_parser(request):
    return render(request, 'parsing.html', {'zipped': zipped})