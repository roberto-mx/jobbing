import connexion
import six

from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing import util


def get_provider_by_id(provider_id):  # noqa: E501
    """get_provider_by_id

    Shows a provider identified by id # noqa: E501

    :param provider_id: id del proveedor de servicios
    :type provider_id: int

    :rtype: UserProfile
    """
    return 'do some magic!'


def get_skills_by_provider_id(provider_id):  # noqa: E501
    """get_skills_by_provider_id

    Show all Service Providers according to their skills # noqa: E501

    :param provider_id: Id de Provider
    :type provider_id: int

    :rtype: List[UserProfile]
    """
    return 'do some magic!'
