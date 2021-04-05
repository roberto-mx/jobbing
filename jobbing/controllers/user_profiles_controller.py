import connexion
import six

from jobbing.models.address import Address  # noqa: E501
from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing import util


def avatar_put(body=None):  # noqa: E501
    """Upload an avatar

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_addres_by_user_id(user_id):  # noqa: E501
    """get_addres_by_user_id

    Displays an Addres of a user # noqa: E501

    :param user_id: Unique identifier
    :type user_id: int

    :rtype: Address
    """
    return 'do some magic!'


def get_user_profile_by_id(uid):  # noqa: E501
    """get_user_profile_by_id

    Displays a User defined by ID # noqa: E501

    :param uid: Unique identifier
    :type uid: str

    :rtype: UserProfile
    """
    return 'do some magic!'


def save_address_profile(body):  # noqa: E501
    """save_address_profile

    Creates an address # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def save_user_profile(body):  # noqa: E501
    """save_user_profile

    Creates a user profile # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_addres_by_user_id(user_id):  # noqa: E501
    """update_addres_by_user_id

    Updates a User attributes # noqa: E501

    :param user_id: Unique identifier
    :type user_id: int

    :rtype: Address
    """
    return 'do some magic!'


def update_user_profile_by_id(uid):  # noqa: E501
    """update_user_profile_by_id

    Updates a User attributes # noqa: E501

    :param uid: Unique identifier
    :type uid: str

    :rtype: UserProfile
    """
    return 'do some magic!'
