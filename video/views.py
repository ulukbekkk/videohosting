from django.shortcuts import render
from .models import *


def get_video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', context={'videos': videos})


def get_video_detail(request, slug):
    video = Video.objects.filter(slug=slug)
    return render(request, 'video_detail.html', context={'video': video})

