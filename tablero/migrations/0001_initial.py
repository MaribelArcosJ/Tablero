# Generated by Django 4.0.3 on 2022-03-20 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control_maquina_semanal',
            fields=[
                ('id_maquina', models.BigAutoField(primary_key=True, serialize=False)),
                ('maquina', models.CharField(max_length=100)),
                ('id_tipo_maquina', models.IntegerField()),
                ('genero', models.IntegerField()),
                ('entrega_premio', models.BooleanField()),
                ('numero_serie', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Gasto_diario',
            fields=[
                ('id_gasto_diario', models.BigAutoField(primary_key=True, serialize=False)),
                ('gasto', models.IntegerField()),
                ('descripción', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario_sucursal_semanal',
            fields=[
                ('id_inventario_sucursal_semanal', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_sucursal', models.IntegerField()),
                ('id_maquina', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id_maquina', models.BigAutoField(primary_key=True, serialize=False)),
                ('maquina', models.CharField(max_length=100)),
                ('id_tipo_maquina', models.IntegerField()),
                ('genero', models.IntegerField()),
                ('entrega_premio', models.BooleanField()),
                ('numero_serie', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.BigAutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=100)),
                ('id_estado', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Periodo_pago',
            fields=[
                ('id_periodo_pago', models.BigAutoField(primary_key=True, serialize=False)),
                ('periodo_pago', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_personal', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('NSS', models.CharField(max_length=11)),
                ('curp', models.CharField(max_length=18)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=100)),
                ('id_sucursal', models.IntegerField()),
                ('id_puesto', models.IntegerField()),
                ('id_tipo_pago', models.IntegerField()),
                ('id_periodo_pago', models.IntegerField()),
                ('usuario', models.CharField(max_length=8)),
                ('contrasena', models.CharField(max_length=8)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Poliza_gasto_diario',
            fields=[
                ('id_gasto', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_gasto_diario', models.IntegerField()),
                ('id_sucursal', models.IntegerField()),
                ('descripción', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id_premio', models.BigAutoField(primary_key=True, serialize=False)),
                ('premio', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id_puesto', models.BigAutoField(primary_key=True, serialize=False)),
                ('peusto', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.BigAutoField(primary_key=True, serialize=False)),
                ('sucursal', models.CharField(max_length=100)),
                ('id_estado', models.IntegerField()),
                ('id_municipio', models.IntegerField()),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_maquina',
            fields=[
                ('id_tipo_maquina', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_maquina', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_pago',
            fields=[
                ('id_tipo_pago', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta_premio',
            fields=[
                ('id_venta_premio', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_premio', models.IntegerField()),
                ('id_maquina', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta_total_maquina',
            fields=[
                ('id_venta_total_maquina', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_maquina', models.IntegerField()),
                ('venta', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estatus', models.BooleanField()),
            ],
        ),
    ]
