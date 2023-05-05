from django.urls import path, include
from rest_framework import routers
from .views import PessoaViewSet, ObjetoViewSet, PossePessoaObjetoViewSet

router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'objetos', ObjetoViewSet)
router.register(r'posses', PossePessoaObjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]