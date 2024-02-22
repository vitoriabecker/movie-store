from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  # classe META: fala para o django qual modelo dever ser usado para criar o formulario
  class Meta:
    model = Post
    fields = ('title', 'text',)