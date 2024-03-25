from django.urls import path
from .views import hash_url, redirect_to_original

urlpatterns = [
    path('', hash_url, name='hash_url'),
    path('<str:hashed_url>/', redirect_to_original, name='redirect_to_original'),
]
