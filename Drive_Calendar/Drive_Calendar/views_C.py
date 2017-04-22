from django.shortcuts import render
from Drive_Calendar.Calendar_EDD import Lista

# ESTE ES EL MANEJO DE VISTAS DE CALENDAR

# ESTRUCTURAS CALENDAR
lista_usuario = Lista.ListaDoble()

# FUNCIONES PARA MANEJAR EL REDIRECCIONAMIENTO ENTRE PAGINAS CALENDAR
def log_In_view(request):

    return render(request, 'LogIn_Calendar.html')

def reg_view(request):

    return render(request, 'Registro_Calendar.html')

# FUNCIONES PARA MANEJAR EL INGRESO DE DATOS EN CALENDAR

def registro_usuarios(request):
    if request.method == 'POST':
        nombre = request.POST['email']
        password = request.POST['password']
        try:
            lista_usuario.agrega_Lista(nombre, password)
            cadena = lista_usuario.cadena_Dot()
            print("-----------Registrando en CALENDAR------------")
            print("Usuario: "+nombre)
            print("Password: "+password)
            print("-----------Fin Registro CALENDAR------------")
        except Exception as inst:
            print("Error en el registro en Drive en Views_C.Py")
    return render(request, 'pr.html',{'var': cadena})