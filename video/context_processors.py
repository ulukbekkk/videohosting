from .models import Video


def video(request):
    return {'cart': Video(request)}