# Generated by Django 3.0.1 on 2020-02-28 01:12

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0027_auto_20200227_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='croppingh',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='croppingv',
        ),
        migrations.AddField(
            model_name='foto',
            name='cropping_horizontal',
            field=image_cropping.fields.ImageRatioField('foto_horizontal', '1200x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping horizontal'),
        ),
        migrations.AddField(
            model_name='foto',
            name='cropping_vertical',
            field=image_cropping.fields.ImageRatioField('foto_vertical', '600x1200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping vertical'),
        ),
    ]
