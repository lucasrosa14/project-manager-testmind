from django.db import models
from projects.models import Project
from users.models import User

class Bug(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Aberto'),
        ('IN_PROGRESS', 'Em Progresso'),
        ('CLOSED', 'Fechado'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Baixa'),
        ('MEDIUM', 'Média'),
        ('HIGH', 'Alta'),
    ]

    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)  # <--- impede exclusão de projeto se houver bug
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    assignee_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_bugs')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='MEDIUM')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
