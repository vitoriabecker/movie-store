from django.shortcuts import render
from .models import Movie
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import MovieForm
from django.shortcuts import redirect

def index(request):
  movies = Movie.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'store/index.html', {'movies': movies})

def movie_detail(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  return render(request, 'store/movie_detail.html', {'movie': movie})

def movie_new(request):
  form = MovieForm()
  return render(request, 'store/movie_edit.html', {'form': form})

def movie_new(request):
  if request.method == "MOVIE":
    form = MovieForm(request.MOVIE)
    if form.is_valid():
      #salvando o formulario
      movies = form.save(commit=False) #commit=false significa que n quero salvar o post ainda- quero adicionar o autor primeiro
      movies.author = request.user #adicionando um autor
      movies.published_date = timezone.now()
      movies.save() #preservando alteracoes e criando um novo post no blog
      return redirect('movie_detail', pk=movies.pk)

  else:
    form = MovieForm()
  return render(request, 'store/movie_edit.html', {'form': form})

def movie_edit(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  if request.method == "MOVIE":
    form = MovieForm(request.MOVIE, instance=movie)
    if form.is_valid():
      movie = form.save(commit=False)
      movie.author = request.user
      movie.puslished_date = timezone.now()
      movie.save()
      return redirect('movie_detail', pk=movie.pk)
  else:
    form = MovieForm(instance=movie)
  return render(request, 'store/movie_edit.html', {'form': form})