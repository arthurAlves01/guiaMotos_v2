from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from usuarios.forms import LoginUsuarioForm
from usuarios.forms import EsqueciSenhaUsuarioForm
from django.contrib.auth import authenticate, login, logout


class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        form = RegistrarUsuarioForm(request.POST)

        if form.is_valid():

            dados_form = form.data

            usuario = User.objects.create_user(dados_form['nome'],
                                               dados_form['email'], dados_form['senha'])

            return redirect('home')

        return render(request, self.template_name, {'form': form})


class LoginUsuarioView(View):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        form = LoginUsuarioForm(request.POST)

        if form.is_valid():

            dados_form = form.data
                        
            u = User.objects.get(email=dados_form['username'])

            user = authenticate(username=u.username, password=dados_form['password'])

            if user is not None:
                login(request, user)
                return redirect('exibir')
            else:
                form.adiciona_erro('Usuario ou senha incorreto')

        return render(request, self.template_name, {'form': form})

def usuarioSair(request):
    logout(request)
    return redirect('home')

class EsqueciSenhaUsuarioView(View):
    template_name = 'esquiciMinhaSenha.html'
    template_name_sucess = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        print("####@@REQ PUT@@####")

        form = EsqueciSenhaUsuarioForm(request.POST)
        print("####@@REQ PUT FORM@@####")

        if form.is_valid():

            dados_form = form.data
            
            u = User.objects.get(email=dados_form['email'])
            u.set_password(dados_form['password'])
            u.save()

            mensagem = 'Senha Alterada!'
            
            return render(request, self.template_name_sucess, {'mensagem': mensagem})

        return render(request, self.template_name, {'form': form})