from rest_framework import serializers
from categories_api.categories.models import Category
from categories_api.utils.validators import depth_level_validator


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_id', 'name', 'description', 'image', 'parent', 'similar_categories')


class CategoriesByDepthSerializer(serializers.Serializer):
    from_level = serializers.IntegerField(min_value=0, validators=[depth_level_validator])


class CategoriesBySimilaritySerializer(serializers.Serializer):
    category_id = serializers.IntegerField(min_value=0)
