from django.urls import path
from .views import index, videofetch

app_name = "video"

urlpatterns = [
    path("", index, name="home"),
    path("video/<str:slug>", videofetch, name="video_fetch"),
]
