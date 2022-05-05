from django.shortcuts import render


def get_video_list(request):
    return render(request, 'video_list.html')
