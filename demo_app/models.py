from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Rating(models.Model):
    value = models.IntegerField(default = 1, validators = [MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)

    def __str__(self):
        return self.content
