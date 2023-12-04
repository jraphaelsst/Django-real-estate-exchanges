from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('novo_imovel/', views.novo_imovel, name='novo_imovel'),
    path('imoveis/', views.imoveis, name='imoveis'),
    path('meus_imoveis/', views.meus_imoveis, name='meus_imoveis'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)