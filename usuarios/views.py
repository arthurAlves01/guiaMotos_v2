from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm

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

		return render(request, self.template_name, {'form' : form})