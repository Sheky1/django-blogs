from django.urls import path
from . import views

app_name = 'demo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('blog/edit/<int:id>/', views.edit, name='edit'),
    path('blog/new/', views.new, name='new'),
    path('register/', views.registration, name='register'),
    path('blog/<int:id>/delete/', views.delete, name='delete'),
    path('blog/newRating/<int:id>/', views.newRating, name='newRating'),
    path('blog/ratings/<int:id>/', views.ratings, name='ratings')
]
