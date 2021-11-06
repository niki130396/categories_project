from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from categories_api.categories.models import Category
from categories_api.categories.api.serializers import CategorySerializer


class CategoriesViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

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
