from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')
def usuarios(request):
    #Salvar os dados da tela
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Gerar a lista de usuarios
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    #Trazer os dados na tela
    return render(request,'usuarios/usuarios.html',usuarios)