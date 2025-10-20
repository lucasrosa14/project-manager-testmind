from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/concluir/', views.project_concluir, name='project_concluir'),
    path('<int:pk>/cancelar/', views.project_cancelar, name='project_cancelar'),
    path("<int:project_id>/concluir/", views.concluir_projeto, name="concluir_projeto"),
    path("<int:project_id>/cancelar/", views.cancelar_projeto, name="cancelar_projeto"),
]
