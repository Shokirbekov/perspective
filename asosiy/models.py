from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    when_created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/category/')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    image = models.ImageField(upload_to='images/post/')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to='images/post_video')

    def __str__(self):
        return self.title
