from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.


def index(request):
    return render(request, "index.html", {'username': get_perfil_logado(request)})


def exibir(request):
    dados = {}
    getMontadoras="http://localhost/api/busca"
    resposta=requests.get(url=getMontadoras)
    montadoras=resposta.json()
    
    for montadora in montadoras:
        getModelos="http://localhost/api/busca/montadora/{}".format(montadora["nome"])
        resposta=requests.get(url=getModelos)
        modelos=resposta.json()
        if isinstance(modelos,dict):
            continue
        for modelo in modelos:
            if modelo["anofabricacao"]=="" or montadora["nome"]=="" or modelo["nomemodelo"]=="":
                continue
            getDados="http://localhost/api/busca/montadora/{}/modelo/{}/ano/{}".format(montadora["nome"], modelo["nomemodelo"], modelo["anofabricacao"])
            resposta=requests.get(url=getDados)
            dadosModelo=resposta.json()
            for k, v in dadosModelo.items():
                if isinstance(v, str):
                    dadosModelo[k] = v.replace("\"","'")
            dados["/".join([montadora["nome"],modelo["nomemodelo"],str(modelo["anofabricacao"])])] = dadosModelo
    dadosFinal = json.dumps(dados)
    return render(request, 'DetalheMoto.html', {'username': get_perfil_logado(request), 'dadosModelos': dadosFinal})


def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')


def get_perfil_logado(request):
    if request.user.is_authenticated:
        return request.user.username
    else:
        return ''