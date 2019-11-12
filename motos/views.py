from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html", {'username': get_perfil_logado(request)})


def exibir(request):
    return render(request, 'DetalheMoto.html', {'username': get_perfil_logado(request)})


def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')


def get_perfil_logado(request):
    if request.user.is_authenticated:
        return request.user.username
    else:
        return ''
        
def exibirmontadora (request):
    URL="http://localhost/api/busca"
    r=requests.get(url=URL)
    data=r.json()
    return render(request, 'DetalheMoto.html', {'exibirmontadora':data})
    