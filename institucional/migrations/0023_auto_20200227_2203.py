# Generated by Django 3.0.1 on 2020-02-28 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0022_trabalho_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='Cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institucional.Cliente'),
        ),
    ]