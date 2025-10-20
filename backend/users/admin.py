from django.contrib import admin
from .models import User  # supondo que você tenha um modelo customizado, caso não use, pode registrar o default

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(User, UserAdmin)
