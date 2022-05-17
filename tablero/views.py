from re import U
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
import tablero.models as modelo

# Create your views here.

def index(request):
    return render(request, 'index.html',{'title':'Inicio'})

def ingresar(request):
    if request.method == 'POST':
        try:
            u = modelo.Personal.objects.get(correo=request.POST.get('mail'))
            if u.contrasena == request.POST['password']:
                request.session['id_personal'] = u.id_personal
                return render(request,'principal.html')
        except modelo.Personal.DoesNotExist:
            return HttpResponse("Your username and password didn't match.")
    return render(request, 'login.html',{'title':'Ingresar'})


def salir(request):
    try:
        del request.session['id_personal']
        return render(request,'login.html')
    except:
        pass
        return render(request, 'index.html',{'title':'Inicio'})
   


def usuario(request):
    return render(request, 'usuario.html',{'title':'Usuario'})


def guardar_usuario(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        apellido_paterno = request.POST['paterno']
        apellido_materno = request.POST['materno']
        NSS = request.POST['nss']
        curp = request.POST['curp']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        id_sucursal = request.POST['sucursal']
        id_puesto = request.POST['puesto']
        id_tipo_pago = request.POST['tipo_pago']
        id_periodo_pago = request.POST['periodo_pago']
        usuario = request.POST['curp']
        contrasena = request.POST['contrasena']

        personal = modelo.Personal(
        nombre = nombre,
        apellido_paterno = apellido_paterno,
        apellido_materno = apellido_materno,
        NSS = NSS,
        curp = curp,
        telefono = telefono,
        correo = correo,
        id_sucursal = id_sucursal,
        id_puesto = id_puesto,
        id_tipo_pago = id_tipo_pago,
        id_periodo_pago = id_periodo_pago,
        usuario = usuario,
        contrasena = contrasena,
        estatus = True
        )

        personal.save()
        return HttpResponse(f"Usuario creado : {personal.nombre} ")
    else: 
        return HttpResponse("No se ha creado el usuario : ")
        
def crear_usuario(request):

    return render(request, 'usuario.html')  

def mostrar_usuario(request):

    usuario = modelo.Personal.objects.get( id= 1)

    return HttpResponse(f"Usuario:")  


def usuarios(request):

    usuarios = modelo.Personal.objects.all()

    return render(request, 'usuarios.html',{
        'usuarios' : usuarios
    })

def editar_usuario(request, id):

    usuario = modelo.Personal.objects.get( id=id )    
    usuario.update()

    return redirect('usuarios') 


def guardar_estado(request):

    if request.method == 'POST':

        estado = request.POST['nombre']
        
        estado = modelo.Estado(
        estado = estado,
        estatus = True
        )

        estado.save()
        return HttpResponse(f"Estado creado : {estado.estado} ")
    else: 
        return HttpResponse("No se ha creado el estado : ")
        
def crear_estado(request):

    return render(request, 'estados.html')  



def guardar_municipio(request):

    if request.method == 'POST':

        municipio = request.POST['municipio']
        
        municipio = modelo.Municipio(
        municipio = municipio,
        estatus = True
        )

        municipio.save()
        return HttpResponse(f"Municipio creado : {municipio.municipio} ")
    else: 
        return HttpResponse("No se ha creado el estado : ")
        
def crear_municipio(request):

    return render(request, 'municipios.html')  


def guardar_pago(request):

    if request.method == 'POST':

        ppago = request.POST['ppago']
        
        ppago = modelo.Periodo_pago(
        periodo_pago = ppago,
        estatus = True
        )

        ppago.save()
        return HttpResponse(f"Periodo pago creado : {ppago.ppago} ")
    else: 
        return HttpResponse("No se ha creado el periodo pago : ")

def crear_pago(request):

    return render(request, 'ppagos.html')  


def guardar_puestos(request):

    if request.method == 'POST':

        puesto = request.POST['puesto']
        
        puesto = modelo.Puesto(
        puesto = puesto,
        estatus = True
        )

        puesto.save()
        return HttpResponse(f"Puesto creado : {puesto.puesto} ")
    else: 
        return HttpResponse("No se ha creado el puesto : ")

def crear_puestos(request):

    return render(request, 'puestos.html')  

def guardar_sucursales(request):

    if request.method == 'POST':

        sucursal = request.POST['sucursal']
        estado = request.POST['estado']
        municipio = request.POST['municipio']
        domicilio = request.POST['domicilio']
        telefono = request.POST['telefono']
        
        sucursal = modelo.Sucursal(
        sucursal = sucursal,
        id_estado= estado,
        id_municipio= municipio,
        domicilio= domicilio,
        telefono= telefono,
        estatus = True
        )

        sucursal.save()
        return HttpResponse(f"Sucursal creada : {sucursal.sucursal} ")
    else: 
        return HttpResponse("No se ha creado la sucursal : ")

def crear_sucursales(request):

    return render(request, 'sucursales.html')  

def guardar_maquinas(request):

    if request.method == 'POST':

        tmaquina = request.POST['maquina']
        
        tmaquina = modelo.Tipo_maquina(
        tipo_maquina = tmaquina,
        estatus = True
        )

        tmaquina.save()
        return HttpResponse(f"Tipo maquina creado : {tmaquina.tipo_maquina} ")
    else: 
        return HttpResponse("No se ha creado el tipo maquina : ")

def crear_maquinas(request):

    return render(request, 'maquinas.html')  

def guardar_tipo_pago(request):

    if request.method == 'POST':

        tpago = request.POST['tpago']
        
        tpago = modelo.Tipo_pago(
        tipo_pago = tpago,
        estatus = True
        )

        tpago.save()
        return HttpResponse(f"Tipo pago creado : {tpago.tpago} ")
    else: 
        return HttpResponse("No se ha creado el tipo pago : ")


def crear_tpago(request):

    return render(request, 'tpago.html') 

def guardar_premio(request):

    if request.method == 'POST':

        premio = request.POST['premio']
        precio = request.POST['precio']
        
        premio = modelo.Premio(
        premio = premio,
        precio = precio,
        estatus = True
        )

        premio.save()
        return HttpResponse(f"Tipo pago creado : {premio.premio} ")
    else: 
        return HttpResponse("No se ha creado el tipo pago : ")

def crear_premio(request):

    return render(request, 'premios.html')  

def guardar_gasto(request):

    if request.method == 'POST':

        gasto = request.POST['ngasto']
        descripcion = request.POST['descripciong']
        
        gasto = modelo.Premio(
        gasto = gasto,
        descripcion = descripcion,
        estatus = True
        )

        gasto.save()
        return HttpResponse(f"Tipo gasto : {gasto.gasto} ")
    else: 
        return HttpResponse("No se ha creado el gasto : ")

def crear_gastod(request):

    return render(request, 'gasto_diario.html')  