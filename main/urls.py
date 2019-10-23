from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.CreateEntry, name="create"),
    path("<pk>/", views.ListArticles, name="list"),
]