from django.db import models

# Create your models here.

class Exercise(models.Model):
    """Modelo de Ejercicio"""
    name = models.CharField(max_length=100, unique=True)  # Nombre del ejercicio
    description = models.TextField()  # Explicación del ejercicio
    muscle_group = models.CharField(max_length=50)  # Grupo muscular (Ej: Pecho, Espalda)
    difficulty = models.CharField(max_length=20, choices=[
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado')
    ])
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)  # Imagen/GIF (Opcional)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name