from django.db import models

# Create your models here.
class Project(models.Model): # creamos la clase
    name = models.CharField(max_length=20) # definimos el tipo de datos
    
class Task(models.Model): # creamos la clase
    title = models.CharField(max_length=200) # definimos el tipo de datos
    description = models.TextField()
    project = models.ForeignKey(Project, # utilizamos esta funcion para relacionar
                                on_delete=models.CASCADE) # si eliminamos la clase, se elimina tambíen
    