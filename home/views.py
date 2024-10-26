from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def index(request):
    return HttpResponse("A view index funcionou, wow!")

from django.http import HttpResponse

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvida por mim mesmo.</h1>")

from django.http import HttpResponse

def contato(request):
    return HttpResponse("<h1>Esta é a página de contato.</h1>")

def ajuda(request):
    return HttpResponse("<h1>Esta é a página de ajuda.</h1>")


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

