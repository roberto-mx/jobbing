import connexion
import six

from jobbing.models.album import Album  # noqa: E501
from jobbing import util


def get_album_by_id(album_id):  # noqa: E501
    """get_album_by_id

    Displays an album defined by ID # noqa: E501

    :param album_id: codigo del album
    :type album_id: int

    :rtype: Album
    """
    return 'do some magic!'


def get_albums():  # noqa: E501
    """get_albums

    Muestra todos los albums disponibles # noqa: E501


    :rtype: List[Album]
    """
    return 'do some magic!'


def save_album_profile(body):  # noqa: E501
    """save_album_profile

    Creates a user profile # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Album.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
