from django.shortcuts import render, redirect
from django.http import HttpResponse 
from principal.models import Produto, Cliente
from .forms import ProdutoForm


from django.contrib import auth, messages
from .models import Cliente
from siteagro import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def  redirect_index (request):
    return redirect('index')

@login_required
def index(request):
    return render(request, "index.html")

def conta(request):
    return render(request,'usuario.html')

def cadastro(request):
    print(request.method)
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        email = request.POST['email']
        endereco = request.POST['endereco']
        senha = request.POST['senha']

        if Cliente.objects.filter(email=email).exists():
            messages.error(request, 'Já existe uma conta com esse e-mail, por favor informe outro email!')
            return redirect('cadastro')
        else:    
            user = Cliente.objects.create_user(username=nome_completo,email=email, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado!')
            return redirect ('login')
    else:
        return render(request,'usuario.html',context={'auth': 'sign-up'})
    
def login(request):
    print(request.method)

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']        

        if Cliente.objects.filter(email=email).exists():
            user = auth.authenticate(request, email=email, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect (settings.LOGIN_REDIRECT_URL)
            else:
                messages.error(request,'E-mail e/ou senha incorretos!')
        else:
           messages.error(request,'E-mail e/ou senha incorretos!')

    return render(request,'usuario.html',context={'auth': 'sign-in'})
    
def logout(request):
    logout(request)
    return redirect('login')

def campo_vazio(campo):
  return not campo.strip()

  
def mercadoria(request):
    lista = Produto.objects.all()
    context = {'mercadoria' :lista}
    return render (request, "mercadoria.html", context)


def about (request):
    return render (request, "about.html")

def add(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST) 
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    return render(request,'forms.html', { 'form' : form})


