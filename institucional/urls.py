from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtrab', views.addtrab, name='addtrab'),
    path('addcliente', views.addcliente, name='addcliente'),
    path('upload', views.upload, name='upload'),
    path('adicionar', views.adicionar, name='adicionar'),
    path('login', views.acessar, name='login'),
    path('conta', views.conta, name='conta'),
    path('login_view', views.login_view, name='login_view'),
    path('<int:x>/fotos', views.fotos, name='fotos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)