from django.contrib import admin
from categories_api.categories import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
