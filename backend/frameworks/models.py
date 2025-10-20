# frameworks/models.py
from django.db import models

class Framework(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
