from django.contrib import admin
from .models import Exercise
# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group', 'difficulty', 'created_at')
    search_fields = ('name', 'muscle_group')

admin.site.register(Exercise, ExerciseAdmin)