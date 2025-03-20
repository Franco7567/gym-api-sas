from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    """CRUD de ejercicios"""
    queryset = Exercise.objects.all().order_by('name')
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
