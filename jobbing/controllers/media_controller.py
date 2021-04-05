import connexion
import six

from jobbing.models.media import Media  # noqa: E501
from jobbing import util


def get_media_by_album_id(album_id):  # noqa: E501
    """get_media_by_album_id

    Lists the media defined by mediaID # noqa: E501

    :param album_id: codigo del album
    :type album_id: int

    :rtype: Media
    """
    return 'do some magic!'


def get_media_by_id(media_id):  # noqa: E501
    """get_media_by_id

    Displays a media defined by the ID # noqa: E501

    :param media_id: codigo de la media
    :type media_id: int

    :rtype: Media
    """
    return 'do some magic!'


def save_media(body):  # noqa: E501
    """save_media

    Creates a media # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Media.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
