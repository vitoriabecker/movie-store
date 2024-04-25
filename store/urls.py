

# aqui, estou importando do DJANGO a funcao URL e todas as minhas VIEWS
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'), # atribuindo 'view' chamada de 'index' a URL raiz, esse padrao URL correspondete a uma string vazia
                                       # e o urlsolver do DJANGO vai ignorar o nome do dominio (127.0.0.1:8000), esse padrao dira ao DJANGO
                                       # que 'views.index' eh o lugar correto de ir se alguem entrar no site pelo endereço 127.0.0.1:8000/
  path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
  path('movie/new/', views.movie_new, name='movie_new'),
  path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
]