from django.contrib import admin
from .models import Trabalho, Foto, Video, Slide, Depoimento, Cliente, Portifolio
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Trabalho, MyModelAdmin)
admin.site.register(Foto, MyModelAdmin)
admin.site.register(Depoimento)
admin.site.register(Cliente)
admin.site.register(Video)
admin.site.register(Portifolio, MyModelAdmin)
admin.site.register(Slide, MyModelAdmin)