from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_json_random, name='create_random_json')
]