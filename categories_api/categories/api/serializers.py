from rest_framework import serializers
from categories_api.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_id', 'name', 'description', 'image', 'parent', 'similar_category')
