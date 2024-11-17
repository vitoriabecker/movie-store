from datetime import *

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from store.forms import SignUpForm, LoginForm, MovieForm, CommentForm, RatingForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Movie, Comment, Rating
from django.contrib.auth.models import Group

# uma 'view' eh o lugar que coloco a logica da minha aplicação.
# ela extrai infos do 'model' que eu criei e entrega elas a um 'template'

def home(request):
  return render(request, 'store/home.html')



def user_signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    
    if form.is_valid():
      messages.success(request, 'Congratulaion! You have become an user.')
      user = form.save()

      try:
        group = Group.objects.get(name='Users')
      except Group.DoesNotExist:
        group = None
        
      user.groups.add(group)
      return redirect('home')
  else:
    form = SignUpForm()
  return render(request, 'registration/signup.html', {'form':form})


def user_login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      form = LoginForm(request=request, data=request.POST)
      
      if form.is_valid():
        user_name = form.cleaned_data['username']
        user_password = form.cleaned_data['password']
        user = authenticate(username=user_name, password=user_password)

        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully!')
          return redirect('home')
    else:
      form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})
  else:
    return redirect('home')
  

def user_logout(request):
  logout(request)
  return redirect('home')  


def movie_list(request):
  template_name = 'movie_list.html'
  movies = Movie.objects.all()
  return render(request, template_name, {"movies":movies})

def movie_detail(request, pk):
  template_name = 'movie_detail.html'
  movie = get_object_or_404(Movie, pk=pk)
  comments = movie.comments.all()

  comment_form = CommentForm()
  return render(request, template_name, {'movie':movie, 
                                         'comments': comments,
                                         'comment_form': comment_form,
                                         'rate_form': RatingForm(),})


@permission_required('store.add_movie', raise_exception=True)
def create_movie(request):
  template_name = 'add_movie.html'

  if request.user.is_authenticated:
    if request.method == 'POST':
      movie_form = MovieForm(request.POST, request.FILES)

      if movie_form.is_valid():
        movie = movie_form.save(commit=False)
        movie.user = request.user

        if 'poster' in request.FILES:
          movie.poster = request.FILES['poster']

        movie.save()

        return redirect('movie_list')
    else:
        movie_form = MovieForm()
    return render(request, template_name, {'movie_form': movie_form})
  else:
    return redirect('login')


@permission_required('store.change_movie', raise_exception=True)
def update_movie(request, pk):
  movie = get_object_or_404(Movie, pk=pk)

  if not request.user.is_authenticated or not request.user.is_superuser:
    return redirect('login')
  
  if request.method == 'POST':
    movie = Movie.objects.get(pk=pk)
    form = MovieForm(request.POST, request.FILES, instance=movie)

    if form.is_valid():
      form.save()
      return redirect('movie_list')
  else:
    form = MovieForm(instance=movie)
  return render(request, 'store/update_movie.html', {'form':form})

    


@permission_required('store.delete_movie', raise_exception=True)
def delete_movie(request, pk):
  movie = get_object_or_404(Movie, pk=pk)

  if request.method == 'POST':
    if request.user.is_authenticated and request.user.is_superuser:
      movie.delete()

      return redirect('movie_list')
  return render(request, 'store/movie_delete.html', {'movie':movie})




def add_comment_to_movie(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  comment_form = CommentForm(data=request.POST)
  
  if comment_form.is_valid():
    new_comment = comment_form.save(commit=False)
    new_comment.movie = movie
    new_comment.save()
    return redirect('movie_detail', pk=pk)
  

  
  

def rate_movie(request, pk):
  if not request.user.is_authenticated:
    return redirect('movie_list')  
  
  if request.method == 'POST':
    rate_form = RatingForm(request.POST)

    if rate_form.is_valid():
      rate = rate_form.cleaned_data['rate']
      movie = get_object_or_404(Movie, pk=pk)
      rating = Rating(movie=movie, user=request.user, rate=rate)

      rating.save()

      return redirect('movie_detail', pk=pk)

  