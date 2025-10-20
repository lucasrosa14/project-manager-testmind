from django.db import models
from clients.models import Client
from frameworks.models import Framework
from users.models import User
from datetime import date


class Project(models.Model):
    TIPO_SISTEMA_CHOICES = [('WEB','Web'),('APP','Mobile'),('API','API'),('DESKTOP','Desktop'),('EMB','Embarcado')]
    ENV_CHOICES = [('LOCAL','Local'),('HOMOLOG','Homologação'),('PROD','Produção')]
    PLANO_CHOICES = [('PACOTE','Pacote'),('PROJETO','Projeto'),('HORA','Por Hora')]
    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando Início'),
        ('EM_EXECUCAO', 'Em Execução'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]

    codigo_projeto = models.CharField(max_length=20, unique=True)
    nome_projeto = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)  # <--- impede exclusão de cliente se houver projeto
    tipo_sistema = models.CharField(max_length=10, choices=TIPO_SISTEMA_CHOICES)
    environment = models.CharField(max_length=10, choices=ENV_CHOICES)
    plano_contratado = models.CharField(max_length=20, choices=PLANO_CHOICES)
    plano_opcao = models.CharField(max_length=50, blank=True)
    horas_contratadas = models.IntegerField(null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status_projeto = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AGUARDANDO')

    framework = models.ForeignKey('frameworks.Framework', on_delete=models.SET_NULL, null=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projetos_criados')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_projeto
    
    @property
    def status_atual(self):
        """Retorna o status baseado na data atual e status definido"""
        if self.status_projeto in ['CONCLUIDO', 'CANCELADO']:
            return self.status_projeto
        if date.today() < self.data_inicio:
            return 'AGUARDANDO'
        return 'EM_EXECUCAO'

    def concluir(self):
        if self.status_projeto not in ['CONCLUIDO', 'CANCELADO']:
            self.status_projeto = 'CONCLUIDO'
            self.save()

    def cancelar(self):
        if self.status_projeto not in ['CONCLUIDO', 'CANCELADO']:
            self.status_projeto = 'CANCELADO'
            self.save()
    
    def delete(self, *args, **kwargs):
        if self.bug_set.exists():  # verifica bugs relacionados
            raise ProtectedError("Não é possível excluir projeto com bugs relacionados.", self)
        return super().delete(*args, **kwargs)
    
