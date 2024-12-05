from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about_time, name='about_time'),
    path('about_pets/', views.about_pets, name='about_pets'),
]