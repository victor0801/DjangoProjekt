from django.shortcuts import render
from django.http import request
# Create your views here.

def index(request):
    return render(request, "index.html")

def page_lista_cursos(request):
    contexto = {
        "cursos":[
        {"nome":"Segurança Da Informação","link":"dSegDaInfo"}, 
        {"nome":"Arquitetura de Software","link":"PADS"}, 
        {"nome":"Jogos Digitais","link":"JD"},
        {"nome":"Redes de Computadores","link":"RC"},
        {"nome":"Sistemas de Informação","link":"SI"}
        ],
        "faculdade":"Faculdade Lorenzinni",
    }
    return render(request, "Lista.html", contexto)

def page_noticias(request):
    return render(request, "noticias.html")

def page_login(request):
    return render(request, "LoginPage.html")

def page_nova_senha(request):
    return render(request, "ForgotPass.html")

def page_cadastro_disciplina(request):
    return render(request, "CadastrarDisciplina.html")

def page_contato(request):
    return render(request, "Contato.html")

def page_cadastro_usuario(request):
    return render(request, "CadastroPage.html")

def page_detalhes_cursos(request):
    return render(request, "DesCurso.html")

def page_detalhes_segdainf(request):
    return render(request, "SegDaInf.html")