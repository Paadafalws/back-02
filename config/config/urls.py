from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mysite.views import QuadrosViewSet,QuadroSerializer,EditarQuadroView, adicionar_quadros,atualizar_quadros
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('Quadros', QuadrosViewSet, basename='Quadros')

urlpatterns = [
    path('Controle/', admin.site.urls),
    path('', include(router.urls)),
    path('Quadros/adicionar/', adicionar_quadros, name='adicionar_quadros'),
    path('Quadros/<int:pk>/', atualizar_quadros, name='atualizar_quadros'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)