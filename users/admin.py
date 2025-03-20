from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'dni', 'is_trainner','is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('dni', 'is_trainner')}),
    )


admin.site.register(User, CustomUserAdmin)