from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'nome_projeto', 'client', 'tipo_sistema', 'environment',
            'plano_contratado', 'plano_opcao', 'horas_contratadas',
            'data_inicio', 'data_fim', 'framework'
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Geração automática do código do projeto
        tipo = self.cleaned_data['tipo_sistema']
        last_project = Project.objects.filter(tipo_sistema=tipo).order_by('id').last()
        next_id = (last_project.id + 1) if last_project else 1
        instance.codigo_projeto = f"{tipo[:3].upper()}-{next_id:03d}"
        if commit:
            instance.save()
        return instance
