# aqui, estou importando do DJANGO a funcao URL e todas as minhas VIEWS
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.home, name='movie_list'), 
  path('about/', views.about, name='about'),

  path('movie/<int:pk>', views.movie_detail, name='movie_detail'),
  path('movie/<int:pk>/publish', views.movie_publish, name='movie_publish'),
  path('movie/create', views.add_movie, name='movie_create'), # mudas essas poha de nome depois
  path('movie/update/<int:pk>', views.update_movie, name='movie_update'),
  path('movie/<int:pk>/delete/', views.delete_movie_confirm, name='movie_delete_confirm'),

  path('movie/<int:pk>/comment', views.add_comment_to_movie, name='add_comment_to_movie'),
  path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
  path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),

  path('signup/', views.user_signup, name='signup'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),

  path('movie/<int:pk>/rating', views.rate_movie, name='rate_movie'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
