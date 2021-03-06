# Generated by Django 3.0.1 on 2020-01-26 06:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.CharField(max_length=2)),
                ('imagem_capa', models.ImageField(blank=True, default='sem_foto.jpg', upload_to='usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='usuarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucional.Trabalho')),
            ],
        ),
    ]
