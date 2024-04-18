from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
  # classe META: fala para o django qual modelo dever ser usado para criar o formulario
  class Meta:
    model = Movie
    fields = ('title', 'synopsis',)