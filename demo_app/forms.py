from django.forms import ModelForm, Form
import django.forms as f
from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category']

