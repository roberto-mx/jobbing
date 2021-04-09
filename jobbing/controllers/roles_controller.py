import connexion
import six

from jobbing.models.role import Role  # noqa: E501
from jobbing import util


def get_roles():  # noqa: E501
    """Lists all user roles

    Show a listing of roles to accesing the API # noqa: E501


    :rtype: List[Role]
    """
    result = []
    result.append(Role(1, 'Admin', 1))
    result.append(Role(2, 'Client', 1))
    result.append(Role(3, 'Provider', 1))
    return result
