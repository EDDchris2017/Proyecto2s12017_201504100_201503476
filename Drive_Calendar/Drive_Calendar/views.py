from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def LogInView(request):

    return render(request, 'LogIn.html')

def Registro(request):

    return render(request, 'Registro.html')