# Generated by Django 3.0.1 on 2020-02-02 04:21

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0005_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('imagem', '1200x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
