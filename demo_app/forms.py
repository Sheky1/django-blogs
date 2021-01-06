from django.forms import ModelForm, Form
import django.forms as f
from .models import Blog, User


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'content']
        
class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


