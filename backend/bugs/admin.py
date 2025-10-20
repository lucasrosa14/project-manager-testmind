from django.contrib import admin
from .models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'author', 'assignee_user', 'created_at')
    list_filter = ('project', 'author', 'assignee_user')
    search_fields = ('name',)
