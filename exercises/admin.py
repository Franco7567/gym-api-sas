from django.contrib import admin
from .models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group', 'difficulty', 'created_at')
    search_fields = ('name', 'muscle_group')
    list_filter = ('difficulty',)

admin.site.register(Exercise, ExerciseAdmin)
