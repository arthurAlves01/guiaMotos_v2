from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='home'),
    re_path(r'^motos$', views.exibir, name='exibir'),
    re_path(r'^login$', views.login, name='login')
]