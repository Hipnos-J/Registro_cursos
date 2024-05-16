from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False, blank=False) 
    nombre = models.CharField(max_length=50, null=False, blank=False )
    apellido = models.CharField(max_length=50, null=False, blank=False )
    fecha_nac = models.DateField(null=False, blank=False )
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_reg = models.DateField()
    creado_por = models.CharField(max_length=50)   
    
class Direccion(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False) 
    calle = models.CharField(max_length=50, null=False, blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False, blank=False )
    ciudad = models.CharField(max_length=50, null=False, blank=False )
    region = models.CharField(max_length=50, null=False, blank=False )
    rut = models.ForeignKey('Estudiante', on_delete=models.CASCADE, null=False, blank=False)



class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, null=False, blank=False, unique=True) 
    nombre = models.CharField(max_length=50, null=False, blank=False )
    version = models.IntegerField()
    rut = models.ForeignKey('Profesor', on_delete=models.CASCADE, null=False, blank=False)

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False, blank=False) 
    nombre = models.CharField(max_length=50, null=False, blank=False )
    apellido = models.CharField(max_length=50, null=False, blank=False )
    fecha_nac = models.DateField(null=False, blank=False )
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_reg = models.DateField()
    creado_por = models.CharField(max_length=50) 