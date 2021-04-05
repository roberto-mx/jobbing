import connexion
import six

from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing import util


def get_provider_by_id(user_profile_id):  # noqa: E501
    """get_provider_by_id

    Shows a provider identified by id # noqa: E501

    :param user_profile_id: id del proveedor de servicios
    :type user_profile_id: int

    :rtype: UserProfile
    """
    return 'do some magic!'


def get_providers_by_skill_id(skill_id):  # noqa: E501
    """get_providers_by_skill_id

    Show all Service Providers according to their skills # noqa: E501

    :param skill_id: Id de Skill
    :type skill_id: int

    :rtype: List[UserProfile]
    """
    return 'do some magic!'
