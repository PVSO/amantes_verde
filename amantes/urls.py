from django.urls import path

from . import views

app_name = 'amantes'

urlpatterns = [
    path('', views.index, name='index'),
    path('logar/', views.logar, name='logar'),
    path('logout/', views.logout, name='logout'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
