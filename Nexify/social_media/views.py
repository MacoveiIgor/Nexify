from django.shortcuts import render
from requests import post

def home(request):
    return render(request, 'social_media/home.html')

def posts(request):
    return render(request, 'social_media/home.html')

def for_you(request):
    posts = post.objects.filter(is_for_you=True)
    return render(request, 'home.html', {'posts': posts, 'active': 'for-you'})

def trending(request):
    posts = post.objects.filter(is_trending=True)
    return render(request, 'home.html', {'posts': posts, 'active': 'trending'})

def following(request):
    posts = post.objects.filter(is_following=True)
    return render(request, 'home.html', {'posts': posts, 'active': 'following'})
