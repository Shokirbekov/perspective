from django.db.models import Count
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from .models import *


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "post": Post.objects.all(),
                "profile": Profile.objects.get(user=request.user),
            }

            return render(request, 'index.html', data)
        else:
            data = {
                "post": Post.objects.all()
            }

            return render(request, 'index.html', data)


class OnePost(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            current_post = Post.objects.get(id=id)

            related_posts = Post.objects.filter(
                category=current_post.category
            ).exclude(id=id)

            data = {
                "post": Post.objects.get(id=id),
                "posts": Post.objects.all(),
                "category": Category.objects.all(),
                "related": related_posts,
                "profile": Profile.objects.get(user=request.user)
            }

            return render(request, 'post.html', data)
        else:
            current_post = Post.objects.get(id=id)

            related_posts = Post.objects.filter(
                category=current_post.category
            ).exclude(id=id)

            data = {
                "post": Post.objects.get(id=id),
                "posts": Post.objects.all(),
                "category": Category.objects.all(),
                "related": related_posts,
            }

            return render(request, 'post.html', data)


class About(View):
    def get(self, request):
        return render(request, 'about.html')
