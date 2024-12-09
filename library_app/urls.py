from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about_time, name='about_time'),
    path('about_pets/', views.about_pets, name='about_pets'),
    path('', views.book_list_view, name='books'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
]