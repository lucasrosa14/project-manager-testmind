from django.urls import path, include
from rest_framework import routers
from .views import (
    ProjectViewSet,
    project_list, project_create, project_detail,
    project_concluir, project_cancelar,
    concluir_projeto, cancelar_projeto
)

# 🔹 Cria o router da API
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # 🔹 Rotas HTML existentes
    path('', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('<int:pk>/concluir/', project_concluir, name='project_concluir'),
    path('<int:pk>/cancelar/', project_cancelar, name='project_cancelar'),
    path('<int:project_id>/concluir/', concluir_projeto, name='concluir_projeto'),
    path('<int:project_id>/cancelar/', cancelar_projeto, name='cancelar_projeto'),

    # 🔹 Rotas da API REST
    path('api/', include(router.urls)),  # 👈 adiciona endpoints REST /projects/
]
