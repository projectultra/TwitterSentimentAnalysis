from django.urls import path
from . import views
from .templates import search
urlpatterns = [
    path('', views.search, name='search'),
    path('fetch_tweets/', views.fetch_tweets, name='fetch_tweets'),
]