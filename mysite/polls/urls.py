from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogue/", views.catalogue, name="catalogue"),
    path("catalogue/<slug:slug>/", views.podcast_detail, name="podcast_detail"),
]