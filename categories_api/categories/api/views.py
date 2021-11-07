from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from categories_api.categories.models import Category
from categories_api.categories.api.serializers import CategorySerializer, CategoriesByDepthSerializer
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema


class CategoriesViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(description="Returns the entire category tree")
    def list(self, request, *args, **kwargs):
        root_nodes = Category.objects.all().get_cached_trees()
        data = []
        for node in root_nodes:
            data.append(self.recursive_node_to_dict(node))
        return Response(data)

    def recursive_node_to_dict(self, node):
        result = self.get_serializer(instance=node).data
        children = [self.recursive_node_to_dict(c) for c in node.get_children()]
        if children:
            result["children"] = children
        return result

    @extend_schema(parameters=[CategoriesByDepthSerializer])
    @action(detail=False, methods=["GET"], url_path="categories-by-depth")
    def get_by_depth(self, request, *args, **kwargs):
        serializer = CategoriesByDepthSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        from_level = serializer.data["from_level"]
        nodes_from_level = Category.objects.filter(level=from_level)
        response = []
        for node in nodes_from_level:
            response.append(self.recursive_node_to_dict(node))
        return Response(response)
