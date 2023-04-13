from django.shortcuts import render


def index(request):

    # produtos = Produto.objects.all()
    # lojas = Loja.objects.all()

    # context = {
    #     'produtos': produtos,
    #     'lojas': lojas
    # }

    return render(request, template_name='index.html')
