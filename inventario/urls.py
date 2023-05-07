from django.urls import path
from . import views


URLS_INDEX = [
    path('', views.IndexView.as_view()),
    path('overview/', views.ApiOverview.as_view(), name='overview'),
]

URLS_PESSOAS = [
    path('api/pessoas/', views.PessoaListView.as_view(), name='pessoa-list'),
    path('api/pessoas/incluir/', views.PessoaCreateView.as_view(), name='pessoa-create'),
    path('api/pessoas/atualizar/<int:pk>/', views.PessoaUpdateView.as_view(), name='pesso-update'),
    path('api/pessoas/excluir/<int:pk>/', views.PessoaDeleteView.as_view(), name='pessoa-delete'),
]

URLS_OBJETOS = [
    path('api/objetos/', views.ObjetoListView.as_view(), name='objeto-list'),
    path('api/objetos/incluir/', views.ObjetoCreateView.as_view(), name='objeto-create'),
    path('api/objetos/atualizar/<int:pk>/', views.ObjetoUpdateView.as_view(), name='objeto-update'),
    path('api/objetos/excluir/<int:pk>/', views.ObjetoDeleteView.as_view(), name='objeto-delete'),
]

URLS_POSSES = [
    path('api/posses/', views.PossePessoaObjetoListView.as_view(), name='posse-list'),
    path('api/posses/incluir/', views.PossePessoaObjetoCreateView.as_view(), name='posse-create'),
    path('api/posses/atualizar/<int:pk>/', views.PossePessoaObjetoUpdateView.as_view(), name='posse-update'),
    path('api/posses/excluir/<int:pk>/', views.PossePessoaObjetoDeleteView.as_view(), name='posse-delete'),
]

urlpatterns = URLS_INDEX + URLS_PESSOAS + URLS_OBJETOS + URLS_POSSES
