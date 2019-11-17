from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^cadastra$',  views.RegistrarUsuarioView.as_view(), name='cadastrar'),
    re_path(r'^login$', views.LoginUsuarioView.as_view(), name='login'),
    re_path(r'^login/resetsenha$', views.EsqueciSenhaUsuarioView.as_view(), name='esqueciSenha'),
    re_path(r'^logout$', views.usuarioSair, name='logout'),
    re_path(r'^excluir$', views.apagarUsuario, name='apagarUsuario'),
    re_path(r'^configurarConta$', views.ConfigurarUsuarioView.as_view(), name='configurarConta')
]