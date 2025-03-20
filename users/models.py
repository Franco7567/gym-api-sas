from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    dni= models.CharField(max_length=8, unique=True, null=False, blank=False)
    email= models.EmailField(max_length=50)
    is_trainner= models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.username} {self.dni}"
    

class Rutinas(models.Model):
    pass


class ejercicios(models.Model):
    pass