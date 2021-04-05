import connexion
import six

from jobbing.models.notification import Notification  # noqa: E501
from jobbing import util


def get_notifications_by_media(media_id):  # noqa: E501
    """get_notifications_by_media

    List all media notifications related to a media # noqa: E501

    :param media_id: Media id
    :type media_id: int

    :rtype: List[Notification]
    """
    return 'do some magic!'


def get_notificationy_by_id(notification_id):  # noqa: E501
    """get_notificationy_by_id

    muestra una notificacion definida por el ID # noqa: E501

    :param notification_id: codigo de la notificacion
    :type notification_id: int

    :rtype: Notification
    """
    return 'do some magic!'


def save_notifications(body):  # noqa: E501
    """save_notifications

    Creates a notification # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Notification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
