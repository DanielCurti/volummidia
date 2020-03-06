# Generated by Django 3.0.1 on 2020-02-25 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institucional', '0020_auto_20200225_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='senha',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
