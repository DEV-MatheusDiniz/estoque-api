from rest_framework import routers

from .views.cliente import ClienteViewSet


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = router.urls
