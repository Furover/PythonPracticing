from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request,'produtos/home.html')
def produtos(request):
    #Salvar os dados da tela
    novo_produto = Produto()
    novo_produto.nome = request.POST.get('nome')
    novo_produto.marca = request.POST.get('marca')
    novo_produto.valor = request.POST.get('valor')
    novo_produto.estoque = request.POST.get('estoque')
    novo_produto.save()
    #Gerar a lista de usuarios
    produtos = {
        'produtos' : Produto.objects.all()
    }
    #Trazer os dados na tela
    return render(request,'produtos/produtos.html',produtos)