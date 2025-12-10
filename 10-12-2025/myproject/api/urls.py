from django.urls import path
from .views import hello, welcome, status, get, post, put, delete

urlpatterns = [
    path('hello/', hello),
    path('welcome/',welcome),
    path('status/',status),
    path('get/',get),
    path('post/',post),
    path('put/',put),
    path('delete/',delete)
]
