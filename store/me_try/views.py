from django.shortcuts import render
from .models import Genre
from itertools import chain
from typing import Iterable

def get_descendants(genre: Genre) -> Iterable[Genre]:
    qs = Genre.objects.filter(parent=genre)
    rs = chain(qs)
    for child in qs:
        rs = chain(rs, get_descendants(child))
    return rs


def show_des(request):
    return render(request,"genres.html",{'des':list(get_descendants(Genre.objects.get(pk=1)))})

def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})
