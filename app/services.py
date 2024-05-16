from .models import Estudiante, Profesor, Curso, Direccion
from django.utils import timezone

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    estudiante = Estudiante.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac,
        activo=activo,
        creacion_registro=timezone.now(),
        modificacion_reg=timezone.now(),
        creado_por=creado_por
    )
    return estudiante

def crear_profesor(rut, nombre, apellido, fecha_nac, activo, creado_por):
    profesor = Profesor.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac,
        activo=activo,
        creacion_registro=timezone.now(),
        modificacion_reg=timezone.now(),
        creado_por=creado_por
    )
    return profesor

def crear_curso(codigo, nombre, version, rut_profesor):
    curso = Curso.objects.create(
        codigo=codigo,
        nombre=nombre,
        version=version,
        rut_id=rut_profesor
    )
    return curso

def crear_direccion(calle, dpto, comuna, ciudad, region, rut_estudiante):
    direccion = Direccion.objects.create(
        calle=calle,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region,
        rut_id=rut_estudiante
    )
    return direccion

def obtiene_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    return estudiante

def obtiene_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    return profesor

def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    return curso

def agrega_profesor_a_curso(rut_profesor, codigo_curso):
    curso = Curso.objects.get(codigo=codigo_curso)
    curso.rut_id = rut_profesor
    curso.save()
    return curso

def agrega_cursos_a_estudiante(rut_estudiante, cursos):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    for curso_codigo in cursos:
        curso = Curso.objects.get(codigo=curso_codigo)
        estudiante.curso_set.add(curso)
    return estudiante

def imprime_estudiante_cursos(rut_estudiante):
    estudiante = Estudiante.objects.get(rut=rut_estudiante)
    cursos = estudiante.curso_set.all()
    for curso in cursos:
        print(curso.codigo, curso.nombre)
