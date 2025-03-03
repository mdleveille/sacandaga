from django.urls import path

from . import views

urlpatterns = [
    path("", views.Calendar, name="calendar"),
    path("events/", views.get_events, name="get_events"),
]