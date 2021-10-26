from django.urls import path
from .views import index, book_search

urlpatterns = [
    path('', index),
    path('book-search/', book_search),
]
