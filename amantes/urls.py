from django.urls import path

from . import views

app_name = 'amantes'

urlpatterns = [
    path('', views.index, name='index')
]
