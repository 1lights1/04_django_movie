from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request): pass

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/create.html', {'form': form})

def detail(request, pk): pass

# F407: 영화 데이터 수정 페이지 및 로직
@require_http_methods(["GET", "POST"]) # NF402: HTTP Method 제한
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk) # 수정할 대상 찾기
    
    if request.method == 'POST':
        # 기존 데이터를 인스턴스로 지정하고 덮어쓰기
        form = MovieForm(request.POST, instance=movie) 
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk) # NF401: URL Name 사용
    else:
        # GET 요청 시 기존 데이터를 폼에 채워서 보여줌
        form = MovieForm(instance=movie) 
        
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

def delete(request, pk): pass