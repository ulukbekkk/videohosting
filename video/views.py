from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import VideoForm


def get_video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', context={'videos': videos})


def get_video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video_detail.html', context={'video': video})

def create_detail(request):
    pass


def create_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            # product = Product.objects.create(**form.cleaned_data)
            return redirect(video.get_absolute_url())
    else:
        form = VideoForm()

    return render(request, 'create_video.html', {'product_form': form})



