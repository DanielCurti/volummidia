from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from image_cropping import ImageRatioField, ImageCropField

class Cliente(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	foto  = models.ImageField(blank=True, upload_to='clientes')

	def __str__(self):
		return self.usuario.first_name

class Portifolio(models.Model):
	imagem = models.ImageField(blank=True, upload_to='portifolio')
	titulo = models.CharField(max_length=30, default='')
	desc   = models.CharField(max_length=200, default='')
	cropping = ImageRatioField('imagem', '1200x600')

	def __str__(self):
		return self.titulo
		
class Trabalho(models.Model):
	titulo       = models.CharField(max_length=200)
	texto        = models.TextField()
	data_criacao = models.DateTimeField(default=timezone.now)
	categoria    = models.CharField(max_length=2)
	cliente      = models.ForeignKey(Cliente, blank=True, null=True, on_delete = models.CASCADE)
	imagem_capa  = models.ImageField(blank=True, upload_to='usuarios', default='sem_foto.png')
	cropping = ImageRatioField('imagem_capa', '1600x800')

	def __str__(self):
		return self.titulo


class Foto(models.Model):
	trabalho = models.ForeignKey(Trabalho, on_delete = models.CASCADE)
	foto_vertical    = models.ImageField(blank=True, upload_to='trabalhos')
	foto_horizontal    = models.ImageField(blank=True, upload_to='trabalhos')
	cropping_horizontal = ImageRatioField('foto_horizontal', '1200x600')
	cropping_vertical = ImageRatioField('foto_vertical', '600x1200')

	def __str__(self):
		return self.trabalho.titulo


class Slide(models.Model):
	imagem = models.ImageField(blank=True, upload_to='slide')
	desc   = models.CharField(max_length=200, default='Sem Descrição')
	cropping = ImageRatioField('imagem', '2400x800')

	def __str__(self):
		return self.desc


class Video(models.Model):
	trabalho = models.ForeignKey(Trabalho, on_delete = models.CASCADE)
	link     = models.CharField(max_length=200)

class Depoimento(models.Model):
	autor = models.ForeignKey(Cliente, on_delete = models.CASCADE)
	texto = models.TextField()
	data  = models.DateField(default=timezone.now)

	def __str__(self):
		return self.autor.usuario.first_name