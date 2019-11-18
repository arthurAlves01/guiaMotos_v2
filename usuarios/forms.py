from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegistrarUsuarioForm(forms.Form):

    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)

    def is_valid(self):

        valid = True

        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        email_exists = User.objects.filter(email=self.data['email']).exists()
        user_exists = User.objects.filter(username=self.data['nome'].lower()).exists()

        if email_exists or user_exists:
            self.adiciona_erro('E-mail ou usuário já cadastrado')
            valid = False
        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class LoginUsuarioForm(forms.Form):

    username = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    def is_valid(self):

        valid = True

        if not super(LoginUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(email=self.data['username']).exists()

        if not user_exists:
            self.adiciona_erro('Usuário não cadastrado')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class EsqueciSenhaUsuarioForm(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    def is_valid(self):

        valid = True

        if not super(EsqueciSenhaUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['name'].lower()).exists()
        user_email_exists = User.objects.filter(email=self.data['email']).exists()

        if not user_exists:
            self.adiciona_erro('Senha não alterada! Verifique os dados inseridos')
            valid = False

        elif not user_email_exists: 
            self.adiciona_erro('Senha não alterada! Verifique os dados inseridos')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class AtualizarCadastro(forms.Form):
    
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    #alteracao do nome do usuario
    def is_valid_username(self):
        
        valid = True

        if not super(AtualizarCadastro, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False
        
        user_exists = User.objects.filter(username=self.data['nome'].lower()).exists()

        if user_exists:
            self.adiciona_erro('Alteração não realizada, nome já cadastrado, tente outro nome')
            valid = False

        return valid

    #alteracao do email do usuario
    def is_valid_email(self):
    
        valid = True

        if not super(AtualizarCadastro, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_email_exists = User.objects.filter(email=self.data['email']).exists()

        if user_email_exists:
            self.adiciona_erro('Alteração não realizada, e-mail já cadastrado, tente outro email')
            valid = False

        return valid

        #alteracao do nome e email do usuario
    def is_valid_user_and_email(self):
    
        valid = True

        if not super(AtualizarCadastro, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False
            
        user_email_exists = User.objects.filter(email=self.data['email']).exists()
        user_exists = User.objects.filter(username=self.data['nome'].lower()).exists()

        if user_email_exists:
            self.adiciona_erro('e-mail já cadastrado, tente outro email')
            valid = False

        if user_exists:
            self.adiciona_erro('nome já cadastrado, tente outro nome')
            valid = False
        
        return valid

    def adicionar_erro_aleatorio(self):
        valid = True
        
        if not super(AtualizarCadastro, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False
        
        self.adiciona_erro('Nenhuma atualização foi realizada pois os dados são iguais aos dados cadastrados')
        valid = False

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)