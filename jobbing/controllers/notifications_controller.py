from flask import abort, Response
import connexion

from jobbing.db import db
from jobbing.DBModels import Notification as DBNotification
from jobbing.models.notification import Notification  # noqa: E501
from jobbing.login import token_required


@token_required
def get_notifications_by_media(media_id):  # noqa: E501
    """get_notifications_by_media

    List all media notifications related to a media # noqa: E501

    :param media_id: Media id
    :type media_id: int

    :rtype: List[Notification]
    """

    notif = DBNotification.query.filter(DBNotification.media_id == media_id).first()

    if notif == None:
        abort(404)

    return Notification(
            account_id=notif.account_id,
            media_id=notif.media_id,
            message=notif.message,
            notification_type_id=notif.notification_type_id,
            status=notif.status,
            title=notif.title)


@token_required
def get_notificationy_by_id(notification_id):  # noqa: E501
    """get_notificationy_by_id

    muestra una notificacion definida por el ID # noqa: E501

    :param notification_id: codigo de la notificacion
    :type notification_id: int

    :rtype: Notification
    """

    notif = DBNotification.query.filter(DBNotification.id == notification_id).first()

    if notif == None:
        abort(404)

    return Notification(
            account_id=notif.account_id,
            media_id=notif.media_id,
            message=notif.message,
            notification_type_id=notif.notification_type_id,
            status=notif.status,
            title=notif.title)


@token_required
def save_notifications(body):  # noqa: E501
    """save_notifications

    Creates a notification # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Notification.from_dict(connexion.request.get_json())  # noqa: E501

        notification = DBNotification(
            account_id=body.account_id,
            media_id=body.media_id,
            message=body.message,
            notification_type_id=body.notification_type_id,
            status=body.status,
            title=body.title)

        db.session.add(notification)
        db.session.commit()

    return (Response(), 201)
