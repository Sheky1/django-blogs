from django.urls import path
from . import views

app_name = 'demo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:id>/', views.blog, name='blog'),
    path('blog/edit/<int:id>/', views.edit, name='edit'),
    path('blog/new/', views.new, name='new')
]
