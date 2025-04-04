from django.db import models

class Exercise(models.Model):
    """Modelo de Ejercicio con soporte para videos externos"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50)
    
    DIFFICULTY_CHOICES = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado')
    ]
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)

    video_url = models.URLField(max_length=200, blank=True, null=True)  # URL del video
    image_url = models.URLField(max_length=200, blank=True, null=True)  # URL de la imagen

    created_at = models.DateTimeField(auto_now_add=True)  # Campo de fecha

    def __str__(self):
        return self.name
