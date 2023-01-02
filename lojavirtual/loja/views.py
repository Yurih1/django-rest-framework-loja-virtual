from rest_framework import viewsets
from loja.models import Roupa
from loja.serializer import RoupaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class RoupasViewSet(viewsets.ModelViewSet):
    """Listando todas as roupas"""
    queryset = Roupa.objects.all()
    serializer_class = RoupaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
