# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.decorators.http import require_http_methods
# from video.models import Video, Favourites
#
# def favourite_add(request, id):
#     video = get_object_or_404(Video, id=id)
#     favor = Favourites.objects.filter(video=video)
#     if favor.favourites.filter(id=request.user.id).exists():
#         favor.favourites.remove(request.user)
#     else:
#         favor.favourites.add(request.user)
#     return redirect(request, 'favourites.html', {'favor': favor})
#
# def favourites_list(request):
#     return render(request, 'favourites.html', {})