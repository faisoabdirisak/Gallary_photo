from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallary, name='gallary'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    # path('search/', views.search_results, name='search_results')
]