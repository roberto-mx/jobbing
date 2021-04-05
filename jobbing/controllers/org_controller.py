import connexion
import six

from jobbing.models.org import Org  # noqa: E501
from jobbing import util


def get_org_by_id(org_id):  # noqa: E501
    """get_org_by_id

    Displays an org # noqa: E501

    :param org_id: Unique identifier
    :type org_id: int

    :rtype: Org
    """
    return 'do some magic!'


def save_org(body):  # noqa: E501
    """save_org

    Creates a new org # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Org.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
