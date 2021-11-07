from django.contrib import admin
from categories_api.categories import models

from mptt.admin import MPTTModelAdmin


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    filter_horizontal = ('similar_categories', )
