from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True)
    similar_categories = models.ManyToManyField(
        "self", blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
