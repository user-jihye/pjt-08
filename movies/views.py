from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)

def filter_genre(request):
    genre_id = request.GET.get('genre')
    genre = Genre.objects.get(pk=genre_id)
    movies = genre.movie_set.all()
    tmp_list = serializers.serialize('json',movies)
    print(tmp_list)

    return JsonResponse(tmp_list,safe=False)
    


@require_safe
def recommended(request):
    pass
