"""django_tablero_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from tablero import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('ingresar/', views.ingresar, name="ingresar"),
    path('cerrar_sesion/', views.salir, name="salir"),    
    
   
    
    path('usuario/', views.usuario, name="usuario"),
    path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
    path('guardar_usuario/', views.guardar_usuario, name="guardar_usuario"),
    path('actualizar_usuario/<int:id_personal>', views.editar_usuario, name="actualizar_usuario"),
    path('mostrar_usuario/', views.mostrar_usuario, name="mostrar_usuario"),
    path('usuarios/', views.usuarios, name="usuarios"),
    
    path('crear_estado/', views.crear_estado, name="crear_estado"),
    path('guardar_estado/', views.guardar_estado, name="guardar_estado"),
    path('crear_municipio/', views.crear_municipio, name="crear_municipio"),
    path('guardar_municipio/', views.guardar_municipio, name="guardar_municipio"),
    path('crear_ppagos/', views.crear_pago, name="crear_ppago"),
    path('crear_puestos/', views.crear_puestos, name="crear_puestos"),
    path('crear_sucursales/', views.crear_sucursales, name="crear_sucursales"),
    path('crear_maquinas/', views.crear_maquinas, name="crear_maquinas"),
    path('crear_tpago/', views.crear_tpago, name="crear_tpago"),
    path('crear_premio/', views.crear_premio, name="crear_premio"),
    path('crear_gastod/', views.crear_gastod, name="crear_gastod"),
    path('crear_gastod/', views.crear_gastod, name="crear_gastod"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)