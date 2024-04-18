from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
  path('movie/new/', views.movie_new, name='movie_new'),
  path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
]