from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'objetos', views.ObjetoViewSet)
router.register(r'posses', views.PossePessoaObjetoViewSet)

URLS_PESSOAS = [
    path('api/pessoas/', views.PessoaListView.as_view(), name='pessoas-list'),
    path('api/pessoas/incluir/', views.PessoaCreateView.as_view(), name='pessoas-create'),
    path('api/pessoas/atualizar/<int:pk>/', views.PessoaUpdateView.as_view(), name='pessoas-update'),
    path('api/pessoas/excluir/<int:pk>/', views.PessoaDeleteView.as_view(), name='pessoas-update'),
]

urlpatterns = URLS_PESSOAS + [
    path('', views.IndexView.as_view()),
    path('overview/', views.ApiOverview.as_view(), name='overview'),
    path('api/', include(router.urls)),
]