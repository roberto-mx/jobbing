import connexion
import six

from jobbing.models.category import Category  # noqa: E501
from jobbing import util


def get_categories():  # noqa: E501
    """get_categories

    Show all categories in the service catalog # noqa: E501


    :rtype: List[Category]
    """
    return 'do some magic!'


def get_category_by_id(category_id):  # noqa: E501
    """get_category_by_id

    Shows a category defined by ID # noqa: E501

    :param category_id: Category Id
    :type category_id: int

    :rtype: Category
    """
    return 'do some magic!'
