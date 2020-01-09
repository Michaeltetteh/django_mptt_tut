from django.urls import path
from .views import show_genres,show_des


urlpatterns = [
    path('genres/', show_des),
]
