# Generated by Django 3.0.1 on 2020-02-22 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0013_auto_20200217_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depoimento',
            name='foto',
        ),
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, upload_to='clientes'),
        ),
    ]
