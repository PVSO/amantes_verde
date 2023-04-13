from django.urls import path

from . import views

app_name = 'loja'

urlpatterns = [
    path('listar/', views.loja_listar, name='loja_listar'),
    path('exibir/', views.loja_exibir, name='loja_exibir'),
    path('<int:loja_pk>/inserir/produto', views.loja_inserir_produto, name='loja_inserir_produto')
]
