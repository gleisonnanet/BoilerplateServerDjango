from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project.apps.core.models import Category
from project.apps.core.models import Ingredient
from project.apps.drf.serializers import CategorySerializer
from project.apps.drf.serializers import IngredientSerializer


class StandardModelViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)


class CategoryViewSet(StandardModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ("id", "name", "start_at", "end_at")


class IngredientViewSet(StandardModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_fields = ("id", "name", "category")
