from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

# Create your views here.

def index(request):
    if request.method != 'GET':
        return redirect('movies:index')

    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def create(request): pass

def detail(request, pk):
    if request.method != 'GET':
        return redirect('movies:index')

    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})

def update(request, pk): pass

def delete(request, pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', pk)