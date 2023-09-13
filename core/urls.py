from rest_framework.routers import DefaultRouter
from .views import TipoViewSet, CategoriaViewSet, ControleViewSet


router = DefaultRouter()
router.register(r'tipos', TipoViewSet),
router.register(r'categorias', CategoriaViewSet)
router.register(r'controles', ControleViewSet)
urlpatterns = router.urls
