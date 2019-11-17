from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from usuarios.forms import LoginUsuarioForm, AtualizarCadastro, EsqueciSenhaUsuarioForm
from django.contrib.auth import authenticate, login, logout


class RegistrarUsuarioView(View):

    template_name = 'registrar.html'
    template_name_sucess = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        form = RegistrarUsuarioForm(request.POST)

        if form.is_valid():

            dados_form = form.data

            usuario = User.objects.create_user(dados_form['nome'].lower(),
                                               dados_form['email'],
                                                dados_form['senha'])

            return render(request, self.template_name_sucess, {'mensagem': 'cadastrado'})

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

        form = EsqueciSenhaUsuarioForm(request.POST)
    
        if form.is_valid():

            dados_form = form.data
            
            u = User.objects.get(email=dados_form['email'])
            u.set_password(dados_form['password'])
            u.save()

            mensagem = 'Senha Alterada!'
            
            return render(request, self.template_name_sucess, {'mensagem': mensagem})

        return render(request, self.template_name, {'form': form})

class ConfigurarUsuarioView(View):
    template_name = 'confiracaoUser.html'
    template_name_sucess = 'index.html'
    def get(self, request, *args, **kwargs):
        nome = request.user.username
        email = request.user.email

        return render(request, self.template_name, {'nome': nome, 'email': email})
    
    def post(self, request, *args, **kwargs):
        
        form = AtualizarCadastro(request.POST)
        mensagem = 'ok'
            #alteracao do nome do usuario
        if request.user.email != form.data['email'] and request.user.username != form.data['nome'].lower():
            dados_form = form.data
            
            usuario = request.user.username

            u = User.objects.get(username=usuario)

            if form.is_valid_user_and_email():
                print(')))))))))))entrou2))))))))))))')
                u.email=dados_form['email']
                u.username=dados_form['nome'].lower()
                u.save()
                return render(request, self.template_name_sucess, {'mensagem': mensagem})
                
            return render(request, self.template_name, {'form': form})

        elif request.user.username != form.data['nome'].lower():
            dados_form = form.data

            usuario = request.user.username
            
            u = User.objects.get(username=usuario)

            if form.is_valid_username():
                u.username=dados_form['nome'].lower()
                u.save()
                return render(request, self.template_name_sucess, {'mensagem': mensagem})

            return render(request, self.template_name, {'form': form})

            #alteracao do email do usuario
        elif request.user.email != form.data['email']:
            dados_form = form.data

            usuario = request.user.username

            u = User.objects.get(username=usuario)

            if form.is_valid_email():
                u.email=dados_form['email']
                u.save()
                return render(request, self.template_name_sucess, {'mensagem': mensagem})

            return render(request, self.template_name, {'form': form})
            
            #alteracao de nome e email
        else :
            form.adicionar_erro_aleatorio()
            return render(request, self.template_name, {'form': form})

def apagarUsuario(request):
    template_name_sucess = 'index.html'

    usuario = request.user.username
    u = User.objects.get(username=usuario)
    logout(request)
    u.delete()
    mensagem = 'excluido'

    return render(request, template_name_sucess, {'mensagem': mensagem})