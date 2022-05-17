from django.db import models

# Create your models here.

class Estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Municipio(models.Model):
    id_municipio = models.BigAutoField(primary_key=True)
    municipio = models.CharField(max_length=100)
    id_estado = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Puesto(models.Model):
    id_puesto = models.BigAutoField(primary_key=True)
    peusto = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Tipo_pago(models.Model):
    id_tipo_pago = models.BigAutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Periodo_pago(models.Model):
    id_periodo_pago = models.BigAutoField(primary_key=True)
    periodo_pago = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Personal(models.Model):
    id_personal = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    NSS = models.CharField(max_length=11)
    curp = models.CharField(max_length=18)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    id_sucursal = models.IntegerField()
    id_puesto = models.IntegerField()
    id_tipo_pago = models.IntegerField()
    id_periodo_pago = models.IntegerField()
    usuario = models.CharField(max_length=8)
    contrasena = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Sucursal(models.Model):
    id_sucursal = models.BigAutoField(primary_key=True)
    sucursal = models.CharField(max_length=100)
    id_estado = models.IntegerField()
    id_municipio = models.IntegerField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Tipo_maquina(models.Model):
    id_tipo_maquina = models.BigAutoField(primary_key=True)
    tipo_maquina = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Maquina(models.Model):
    id_maquina = models.BigAutoField(primary_key=True)
    maquina = models.CharField(max_length=100)
    id_tipo_maquina = models.IntegerField()
    genero = models.IntegerField()
    entrega_premio = models.BooleanField()
    numero_serie = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Control_maquina_semanal(models.Model):
    id_maquina = models.BigAutoField(primary_key=True)
    maquina = models.CharField(max_length=100)
    id_tipo_maquina = models.IntegerField()
    genero = models.IntegerField()
    entrega_premio = models.BooleanField()
    numero_serie = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Premio(models.Model):
    id_premio = models.BigAutoField(primary_key=True)
    premio = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Venta_premio(models.Model):
    id_venta_premio = models.BigAutoField(primary_key=True)
    id_premio = models.IntegerField()
    id_maquina = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Inventario(models.Model):
    id_inventario = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Inventario_sucursal_semanal(models.Model):
    id_inventario_sucursal_semanal = models.BigAutoField(primary_key=True)
    id_sucursal = models.IntegerField()
    id_maquina = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Gasto_diario(models.Model):
    id_gasto_diario = models.BigAutoField(primary_key=True)
    gasto = models.IntegerField()
    descripción = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Poliza_gasto_diario(models.Model):
    id_gasto = models.BigAutoField(primary_key=True)
    id_gasto_diario = models.IntegerField()
    id_sucursal = models.IntegerField()
    descripción = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()

class Venta_total_maquina(models.Model):
    id_venta_total_maquina = models.BigAutoField(primary_key=True)
    id_maquina = models.IntegerField()
    venta = models.DecimalField(max_digits=11, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_actualizacion = models.DateTimeField(auto_now = True)
    estatus = models.BooleanField()