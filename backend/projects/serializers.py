from rest_framework import serializers
from .models import Project
from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'contact_email', 'contact_phone']


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source='client',
        write_only=True
    )
    status_atual = serializers.CharField(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'codigo_projeto',
            'nome_projeto',
            'tipo_sistema',
            'environment',
            'plano_contratado',
            'plano_opcao',
            'horas_contratadas',
            'data_inicio',
            'data_fim',
            'status_projeto',
            'status_atual',
            'framework',
            'criado_por',
            'client',
            'client_id',
            'created_at'
        ]
