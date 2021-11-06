from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField()
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="parent", blank=True, null=True)
    similar_category_id = models.ManyToManyField(
        "self", related_name="similar_categories", blank=True
    )
