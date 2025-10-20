from django.contrib import admin
from .models import Project

@admin.action(description='Concluir projeto selecionado')
def concluir_projetos(modeladmin, request, queryset):
    for projeto in queryset:
        projeto.concluir()

@admin.action(description='Cancelar projeto selecionado')
def cancelar_projetos(modeladmin, request, queryset):
    for projeto in queryset:
        projeto.cancelar()

from django.contrib import admin
from .models import Project
from django.utils import timezone

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_projeto',
        'nome_projeto',
        'client',
        'framework',
        'data_inicio',
        'data_fim',
        'status_atual',
    )
    list_filter = (
        'client',
        'status_projeto',
        'framework',
        'data_inicio',
    )
    search_fields = ('codigo_projeto', 'nome_projeto', 'client__nome_cliente')
    readonly_fields = ('created_at',)
    actions = ['concluir_projeto', 'cancelar_projeto']

    @admin.action(description="Marcar projetos selecionados como Concluídos")
    def concluir_projeto(self, request, queryset):
        for project in queryset:
            project.concluir()
        self.message_user(request, "Projetos marcados como concluídos com sucesso.")

    @admin.action(description="Marcar projetos selecionados como Cancelados")
    def cancelar_projeto(self, request, queryset):
        for project in queryset:
            project.cancelar()
        self.message_user(request, "Projetos marcados como cancelados com sucesso.")

