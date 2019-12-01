from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from .models import Favoritos
# Create your views here.


def index(request):
    return render(request, "index.html", {'username': get_perfil_logado(request)})


def exibir(request, montadora="", modelo="", ano=""):
    dados_favorito = None
    if montadora and modelo and ano:
        dados_favorito = {"montadora": montadora, "modelo": modelo, "ano": ano}
    print(dados_favorito)
    dados = {}
    getMontadoras="http://localhost/api/busca"
    resposta=requests.get(url=getMontadoras)
    if resposta.status_code == 200:
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
        return render(request, 'DetalheMoto.html', {'username': get_perfil_logado(request), 'dadosModelos': dadosFinal, "dados_favorito": dados_favorito})
    return render(request, 'DetalheMoto.html', {'username': get_perfil_logado(request)})


def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')


def get_perfil_logado(request):
    if request.user.is_authenticated:
        return request.user.username.title()
    else:
        return ''

def get_id_perfil_logado(request):
    if request.user.is_authenticated:
        return request.user.id
    else:
        return 0

def favoritos(request):
    '''
    Renderiza a tela de favoritos
    '''
    id_logado = get_id_perfil_logado(request)
    if id_logado == 0:
        return render(request, 'favoritos.html', {'username': id_logado})
        
    lista_favoritos = Favoritos.objects.filter(id_usuario=id_logado)
            
    return render(request, 'favoritos.html', {'username': get_perfil_logado(request), 'lista_favoritos': lista_favoritos})

def salva_favorito(request):
    '''
    Salva os dados do modelo favotiro no banco de dados
    '''
    fav_montadora = request.GET['montadora']
    fav_modelo = request.GET['modelo']
    fav_ano = request.GET['ano']
    usuario = get_id_perfil_logado(request)
    if usuario == 0:
        return JsonResponse({"logado":False})
    favoritos_usuario = Favoritos.objects.filter(id_usuario=usuario)
    modelo_atual_existe = Favoritos.objects.filter(montadora=fav_montadora, modelo=fav_modelo, ano_modelo=fav_ano)
    if not modelo_atual_existe:
        Favoritos.objects.create(montadora=fav_montadora, modelo=fav_modelo, ano_modelo=fav_ano, id_usuario=usuario).save()
        flag_modelo_atual_existe = False
    else:
        flag_modelo_atual_existe = True
        pass
    retorno = {
        "existe": flag_modelo_atual_existe,
        "logado": True
    }
    
    
    return JsonResponse(retorno)
