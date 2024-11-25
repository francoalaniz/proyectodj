from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, verbose_name='Nombre')
    ap = models.CharField(max_length=100, verbose_name='Apellido')
    am = models.CharField(max_length=500, verbose_name='Encargo')
    dir = models.TextField(null=True, verbose_name='Dirección')
    tel = models.TextField(null=True, verbose_name='Telefono')
    
    def __str__(self):
        fila="Id: "+ str(self.id)+ "-"+ "Nombre: " +self.nom + "-" "Apellido Paterno: " +self.ap
        return fila 
