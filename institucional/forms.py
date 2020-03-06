from django import forms 
from django.utils import timezone
from datetime import datetime, timedelta

class AddTrab(forms.Form) :
    CATEGORIA = (
        ('PS', 'Para Seleção'),
        ('CM', 'Casamento'),
        ('15', '15 Anos'),
        ('ET', 'Estudio'),
    )

    titulo    = forms.CharField(label="Titulo", max_length=30)
    descricao = forms.CharField(label="Texto sobre o trabalho", max_length=500)
    capa      = forms.FileField(label="Foto de Capa")
    categoria  = forms.CharField(label='Categoria', widget=forms.Select(choices=CATEGORIA))
    filesh      = forms.FileField(label="Fotos")
    filesv      = forms.FileField(label="Fotos")

    titulo.widget.attrs['placeholder'] = 'Titulo do Trabalho'
    descricao.widget.attrs['placeholder'] = 'Texto sobre o trabalho'
    titulo.widget.attrs['class'] = 'form-control'
    descricao.widget.attrs['class'] = 'form-control'
    filesh.widget.attrs['multiple'] = 'multiple'
    filesv.widget.attrs['multiple'] = 'multiple'
    categoria.widget.attrs['class'] = 'custom-select'

class UsuarioSenha(forms.Form) :
    login = forms.CharField(label="", max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput(), label="", max_length=20)

    login.widget.attrs['placeholder'] = 'Login'
    senha.widget.attrs['placeholder'] = 'Senha'
    login.widget.attrs['class'] = 'form-control'
    senha.widget.attrs['class'] = 'form-control'


class AddCliente(forms.Form) :
    login = forms.CharField(label="", max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput(), label="", max_length=20)
    email = forms.CharField(label="", max_length=50)
    foto  = forms.FileField(label="Foto de Capa")
    nome = forms.CharField(label="", max_length=30)
    sobrenome = forms.CharField(label="", max_length=30)


    login.widget.attrs['placeholder'] = 'Login'
    senha.widget.attrs['placeholder'] = 'Senha'
    login.widget.attrs['class'] = 'form-control'
    senha.widget.attrs['class'] = 'form-control'
