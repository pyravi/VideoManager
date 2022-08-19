from django.shortcuts import render
from .models import TitleManager, VideoManager

# Create your views here.


def index(request):
    titles = TitleManager.objects.all()
    context = {
        "object_list": titles
    }
    return render(request, "index.html", context)


def videofetch(request, slug=None):
    if slug:
        result =  VideoManager.objects.filter(parent_title__slug=slug)
    else:
        result = VideoManager.objects.all()

    context = {
        "object_list": result
    }
    return render(request, "videolist.html", context)
