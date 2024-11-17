# aqui, estou importando do DJANGO a funcao URL e todas as minhas VIEWS
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.home, name='home'), 

  path('movie/', views.movie_list, name='movie_list'),
  path('movie/<int:pk>', views.movie_detail, name='movie_detail'),
  path('movie/create', views.create_movie, name='movie_create'),
  path('movie/update/<int:pk>', views.update_movie, name='movie_update'),
  path('movie/<int:pk>/delete/', views.delete_movie, name='movie_delete'),
  path('movie/<int:pk>/rating', views.rate_movie, name='rate_movie'),
  path('movie/<int:pk>/comment', views.add_comment_to_movie, name='add_comment_to_movie'),

  path('signup/', views.user_signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
