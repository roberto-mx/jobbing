import connexion
import six
from flask import abort

from jobbing.DBModels import Category as DBCategory
from jobbing.models.category import Category  # noqa: E501
from jobbing import util


def get_categories():  # noqa: E501
    """get_categories

    Show all categories in the service catalog # noqa: E501


    :rtype: List[Category]
    """

    categories = DBCategory.query.all()
    results = [
        Category(category.id, category.name, category.description, category.status) for category in categories]
    return results


def get_category_by_id(category_id):  # noqa: E501
    """get_category_by_id

    Shows a category defined by ID # noqa: E501

    :param category_id: Category Id
    :type category_id: int

    :rtype: Category
    """
    category = DBCategory.query.filter(DBCategory.id == category_id).first()

    if category == None:
        abort(404)
    return Category(category.id, category.name, category.description, category.status)
