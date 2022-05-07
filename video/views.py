from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from config import settings
from .models import *
from .forms import CreateVideoForm, UpdateVideoForm


def get_video_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    videos = Video.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        videos = videos.filter(category=category)

    paginator = Paginator(videos, settings.PAGINATOR_NUM)
    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)

    return render(request, 'video_list.html', context={'videos': videos})


def get_video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'video_detail.html', context={'video': video})


@login_required(login_url='login')
def create_video(request):
    if request.method == 'POST':
        form = CreateVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            # product = Product.objects.create(**form.cleaned_data)
            return redirect(video.get_absolute_url())
    else:
        form = CreateVideoForm()

    return render(request, 'create_video.html', {'create_form': form})


def update_video(request, id):
    video = get_object_or_404(Video, id=id)
    video_form = UpdateVideoForm(request.POST or None, request.FILES or None, instance=video)
    if video_form.is_valid():
        video = video_form.save()
        return redirect(video.get_absolute_url())
    return render(request, 'update_video.html', locals())


def detele_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
        return redirect("video_list_url")
    return render(request, 'delete_video.html', locals())



def search_video(request):
    category = None
    categories = Category.objects.all()
    video = None
    search = request.GET.get('search')
    if search:
        video = Video.objects.filter(Q(title__icontains=search) |
                                          Q(description__icontains=search)
                                          )
    context = {
        'videos': video,
        'categories': categories,
        'category': category
    }
    return render(
        request,
        'video_list.html',
        context
    )