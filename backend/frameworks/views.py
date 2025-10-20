from rest_framework import viewsets
from .models import Framework
from .serializers import FrameworkSerializer

class FrameworkViewSet(viewsets.ModelViewSet):
    queryset = Framework.objects.all().order_by('name')
    serializer_class = FrameworkSerializer
