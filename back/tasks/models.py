from django.db import models

from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    done = models.BooleanField()

    def __str__(self):
        return self.titulo
