from rest_framework.viewsets import ModelViewSets

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSets):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer