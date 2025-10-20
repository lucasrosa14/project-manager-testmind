from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone', 'created_at')
    search_fields = ('name', 'contact_email')
