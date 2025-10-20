from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.bug_create, name='bug_create'),
]
