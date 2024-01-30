from django.urls import path, include

from . import views

app_name = 'loja'

urlpatterns = [
    # path('logar/', views.loja_logar, name='logar'),
    # path('cadastrar/', views.loja_cadastrar, name='cadastrar'),
    path('listar/', views.loja_listar, name='listar'),
    path('exibir/', views.loja_exibir, name='exibir'),
    path('inserir/produto', views.cadastrar_produtos, name='cadastrar_produtos'),
]
