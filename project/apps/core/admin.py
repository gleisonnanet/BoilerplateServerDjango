from django.contrib import admin
from project.apps.core.models import Category
from project.apps.core.models import Ingredient
from project.support.django_helpers import CustomModelAdminMixin
from project.support.django_helpers import ExportCsvMixin


@admin.register(Category)
class CategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]


@admin.register(Ingredient)
class IngredientAdmin(CustomModelAdminMixin, admin.ModelAdmin, ExportCsvMixin):
    list_filter = ["category", "created_at", "updated_at"]
    actions = ["export_as_csv"]
