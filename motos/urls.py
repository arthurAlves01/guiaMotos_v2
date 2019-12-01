from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='home'),
    re_path(r'^motos$', views.exibir, name='exibir'),
    path('motos/<str:montadora>/', views.exibir, name='exibir'),
    path('motos/<str:montadora>/<str:modelo>/<str:ano>', views.exibir, name='exibir'),
    re_path(r'^favoritos$', views.favoritos, name='favoritos'),
    re_path(r'^salvarFavorito$', views.salva_favorito, name="salva_favorito")
]