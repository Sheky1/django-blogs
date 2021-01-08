from django.forms import ModelForm, Form
import django.forms as f
from .models import Blog, User, Rating


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'content']
        
class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['value']


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


