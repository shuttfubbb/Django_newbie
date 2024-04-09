from django.urls import path
from . import views

urlpatterns = [
    path('search/results', views.bookSearchApi, name='search_results'),
]