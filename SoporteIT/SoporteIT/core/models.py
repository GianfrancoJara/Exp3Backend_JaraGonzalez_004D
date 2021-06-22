from django.db import models

# Create your models here.

class Contratacion(models.Model):
    idContratacion =models.IntegerField(primary_key=True, verbose_name='Id de la Contratacion')
    tipoContratacion = models.CharField(max_length=50, verbose_name='Tipo de Contratacion')


    def __str__(self):
        return self.tipoContratacion

# Modelo de Contratacion

class Solicitud(models.Model): 
    rut = models.CharField(max_length=10,primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    region = models.CharField(max_length=30, verbose_name='Region')
    comuna = models.CharField(max_length=30, verbose_name='Comuna')
    correo = models.CharField(max_length=30, verbose_name='Correo Electronico')
    contratacion = models.ForeignKey(Contratacion, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=512,null=True, verbose_name='Comentario')

    def __str__(self):
        return self.rut
    


