from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('nova_permuta/', views.nova_permuta, name='nova_permuta'),
    path('permutas/', views.permutas, name='permutas'),
    path('minhas_permutas/', views.minhas_permutas, name='minhas_permutas'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
