from .models import Video
from myuser.models import User


def video(request):
    return {'cart': Video(request)}

def favourites(request):
    if request.user.is_authenticated:
        return {"fav": request.user.fav.all()}
    return {}

def get_base_html(request):
    video = Video.objects.all().count()
    user = User.objects.all().count()

    # count_video = list(video).count()
    return {'video_count': video, 'users_count': user}