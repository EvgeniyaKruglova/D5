from django import forms
from .models import Post, Category, Author
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
   Category = forms.ModelMultipleChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
   )

   class Meta:
       model = Post
       fields = [
           'author',
           'type',
           'title',
           'text',
       ]
       labels={
               'author':'Автор',
               'type':'Тип',
               'title':'Заголовок',
               'text':'Текст',
               }
