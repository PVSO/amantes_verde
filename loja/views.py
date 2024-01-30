from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import render


def loja_listar(request):
    pass


def loja_exibir(request):
    return render(request, template_name='exibir.html')

# @login_required
@has_permission_decorator('cadastrar_produtos')
def cadastrar_produtos(request):
    return render(request, template_name='cadastrar_produtos.html')
