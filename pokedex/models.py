from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name= models.CharField(max_length=30, null=False)
    type= models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4,max_digits=6)
    height = models.DecimalField(decimal_places=4,max_digits=6)

    def __str__(self):
        return self.name
    
## Entrenador
# Nombre
# Apellido
# Nivel
# Fecha de Nacimiento Date Field()

class Entrenador(models.Model):
    # Campos del modelo
    nombre = models.CharField(max_length=50)          # Nombre del entrenador
    apellido = models.CharField(max_length=50)        # Apellido del entrenador
    nivel = models.IntegerField()                     # Nivel (tipo entero)
    fecha_nacimiento = models.DateField()             # Fecha de nacimiento

    # Representación en texto del objeto
    def __str__(self):
        return f"{self.nombre} {self.apellido}"