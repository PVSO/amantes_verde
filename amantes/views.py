from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):

    # produtos = Produto.objects.all()
    # lojas = Loja.objects.all()

    # context = {
    #     'produtos': produtos,
    #     'lojas': lojas
    # }

    return render(request, template_name='index.html')


def cadastrar(request):
    return render(request, template_name='cadastro.html')


def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('loja:cadastrar_produtos'))
        return render(request, 'registration/login.html')

    elif request.method == 'POST':
        login = request.POST.get('username')
        senha = request.POST.get('password')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            return HttpResponse('Não foi possível se autenticar')

        auth.login(request, user)
        return redirect(reverse('loja:cadastrar_produtos'))


def logout(request):
    request.session.flush()
    return redirect(reverse('amantes:logar'))
