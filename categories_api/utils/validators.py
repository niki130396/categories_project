from categories_api.utils.common import get_max_category_tree_depth
from rest_framework.exceptions import ValidationError


def depth_level_validator(from_level: int):
    top_level = get_max_category_tree_depth()
    if from_level > top_level:
        raise ValidationError(f"Chosen level exceeds tree depth. Tree depth is {top_level}.")
