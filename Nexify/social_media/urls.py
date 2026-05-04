from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('for-you', views.for_you, name='for-you'),
    path('trending', views.trending, name='trending'),
    path('following', views.following, name='following'),
]