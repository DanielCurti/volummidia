# Generated by Django 3.0.1 on 2020-02-02 05:02

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0008_auto_20200202_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='cropping',
        ),
        migrations.AddField(
            model_name='slide',
            name='list_page_cropping',
            field=image_cropping.fields.ImageRatioField('imagem', '200x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='list page cropping'),
        ),
    ]