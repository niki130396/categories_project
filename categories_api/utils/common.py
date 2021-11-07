from categories_api.categories.models import Category


def get_max_category_tree_depth():
    obj = Category.objects.distinct("level").order_by("-level").first()
    return obj.level
