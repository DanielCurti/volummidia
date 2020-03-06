# Generated by Django 3.0.1 on 2020-02-23 05:22

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0015_depoimento_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, upload_to='portifolio')),
                ('titulo', models.CharField(default='', max_length=30)),
                ('desc', models.CharField(default='', max_length=200)),
                ('cropping', image_cropping.fields.ImageRatioField('imagem', '1200x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
            ],
        ),
    ]