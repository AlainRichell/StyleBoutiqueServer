from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, ImagenViewSet, AfiliadoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'imagenes', ImagenViewSet)
router.register(r'afiliados', AfiliadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
