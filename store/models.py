from django.conf import settings
from django.db import models
from django.utils import timezone

class Movie(models.Model): # Objeto: define o modelo | models.Model diz que Post eh um modelo de Django
                          # entao o Django sabe que ele deve ser salvo no banco de dados.
  director = models.CharField(max_length=200)
  title = models.CharField(max_length=200) # define um texto com um numero limitado de chars
  synopsis = models.TextField() # para textos sem limite fixo, ideal para conteudo de um blog
  created_date = models.DateTimeField(default=timezone.now) 
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title
