from django.contrib import admin
from .models import Movie, Comment, Rating

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Rating)

class MovieAdmin(admin.ModelAdmin):
  list_display = ['pk', 'user', 'director', 'title', 'poster', 'synopsis', 'year']

class CommentAdmin(Comment):
  list_display = ('movie', 'author', 'text', 'created_date', 'active')
  list_filter = ('active', 'created_date')
  search_field = ('author', 'text') 
  actions = ['approve_comments']

  def approve_comments(self, request, queryset):
    queryset.update(active=True)