from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet
from clients.views import ClientViewSet
from bugs.views import BugViewSet

# 🔹 Router DRF centralizado
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'bugs', BugViewSet, basename='bugs')

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔹 Rotas de API centralizadas
    path('api/', include(router.urls)),

    # 🔹 Mantém as rotas manuais (caso ainda use templates)
    path('projects/', include('projects.urls')),
    path('clients/', include('clients.urls')),
    path('bugs/', include('bugs.urls')),
]
