from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('formulaire/', views.formulaire),
    path('bonjour/', views.bonjour),
    path('main/', views.main),
    path('ajout', views.ajout),
    path('traitement/', views.traitement),
]