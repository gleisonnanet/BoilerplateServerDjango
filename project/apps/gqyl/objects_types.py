from graphene_django.types import DjangoObjectType

from project.apps.core.models import Category
from project.apps.core.models import Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
