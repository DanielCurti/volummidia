from django.shortcuts import render
from django.http import HttpResponseRedirect
from institucional.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import *


def index(request):
	lista_slides = Slide.objects.all()
	lista_depoimentos = Depoimento.objects.all()
	lista_portifolio = Portifolio.objects.all()
	contexto = {'lista_slides': lista_slides, 'lista_depoimentos': lista_depoimentos, 'lista_portifolio': lista_portifolio}
	return render(request, "index.html", contexto)


def addtrab(request):
	if request.user.is_superuser:
		form = AddTrab()
		cliente = Cliente.objects.all()
		contexto = {'form': form, 'cliente': cliente}
		return render(request, "addtrab.html", contexto)
	else:
		return HttpResponseRedirect('/')


def addcliente(request):
	if request.user.is_superuser:
		form = AddCliente()
		contexto = {'form': form}
		return render(request, "addcliente.html", contexto)
	else:
		return HttpResponseRedirect('/')


def upload(request):
	if request.user.is_superuser:
		form = AddTrab(request.POST, request.FILES)
		if form.is_valid():
			t = Trabalho()
			t.titulo = form.cleaned_data['titulo']
			t.texto = form.cleaned_data['descricao']
			t.categoria = form.cleaned_data['categoria']
			c = Cliente.objects.get(usuario=(request.POST.get('cliente')))
			t.cliente   = c
			t.data_criacao = timezone.now()
			t.imagem_capa = form.cleaned_data['capa']
			t.save()
			for f in request.FILES.getlist('filesh'):
				ft = Foto()
				ft.trabalho = t
				ft.foto_horizontal = f
				ft.save()
			for f in request.FILES.getlist('filesv'):
				ft = Foto()
				ft.trabalho = t
				ft.foto_vertical = f
				ft.save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def adicionar(request):
	if request.user.is_superuser:
		form = AddCliente(request.POST, request.FILES)
		if form.is_valid():
			login = form.cleaned_data['login']
			senha = form.cleaned_data['senha']
			nome = form.cleaned_data['nome']
			sobrenome = form.cleaned_data['sobrenome']
			email = form.cleaned_data['email']
			usuario = User.objects.create_user(login, email, senha)
			usuario.first_name = nome
			usuario.last_name = sobrenome
			usuario.is_staff = True
			usuario.save()

			p = Cliente()
			p.usuario = usuario
			p.foto = form.cleaned_data['foto']
			p.save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def acessar(request):
	if request.user.is_authenticated:
		form = UsuarioSenha()
		contexto = {'form': form}
		return render(request, "login.html", contexto)
	else:
		form = UsuarioSenha()
		contexto = {'form': form}
		return render(request, "login.html", contexto)


def login_view(request):
    if request.method == 'POST':
        form = UsuarioSenha(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['login']
            senha = form.cleaned_data['senha']

            Usuario = authenticate(request, username=usuario, password=senha)
            if Usuario is not None:
                login(request, Usuario)
                return HttpResponseRedirect('conta')
            else:
                contexto = {"form": form, "mensagem": "Usuário ou senha inválida" }
                return render(request, 'login.html', contexto)
        else:
            return HttpResponse("Formulário inválido")
    else:
        form = UsuarioSenha()
        contexto = {"form": form}
        return render(request, 'login.html', contexto)


def conta(request):
	if request.user.is_authenticated:
		usuario  = Cliente.objects.get(usuario=request.user)
		trabalhos = Trabalho.objects.filter(cliente=usuario)
		contexto = {"trabalhos": trabalhos}
		return render(request, 'conta.html', contexto)
	else:
		return HttpResponseRedirect('/')



def fotos(request, x):
	if request.user.is_authenticated:
		trabalho = Trabalho.objects.get(id=x)
		fotos    = Foto.objects.filter(trabalho=trabalho)
		print(request.user)
		print(trabalho.cliente.usuario)
		if request.user == trabalho.cliente.usuario:
			contexto = {"fotos": fotos}
			return render(request, 'fotos.html', contexto)
		else:
			return HttpResponseRedirect('/login')
	else:
		return HttpResponseRedirect('/')