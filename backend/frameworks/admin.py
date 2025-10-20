# frameworks/admin.py
from django.contrib import admin
from .models import Framework

@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'language', 'created_at')  # campos existentes
    list_filter = ('language', 'created_at')  # filtros válidos
    search_fields = ('name', 'version', 'language')
