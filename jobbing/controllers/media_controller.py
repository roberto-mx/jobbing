from flask import abort, Response
from flask_login import login_required
import connexion
import six

from jobbing.db import db
from jobbing.DBModels import Media as DBMedia
from jobbing.models.media import Media  # noqa: E501
from jobbing import util


@login_required
def get_media_by_album_id(album_id):  # noqa: E501
    """get_media_by_album_id

    Lists the media defined by mediaID # noqa: E501

    :param album_id: codigo del album
    :type album_id: int

    :rtype: Media
    """
    media = DBMedia.query.filter(DBMedia.album_id == album_id).first()

    if media == None:
        abort(404)
    return Media(media.id, media.media, media.link, media.title, media.size, media.duration, media.created, media.media_type, media.views, media.likes, media.owner_id, media.album_id)


@login_required
def get_media_by_id(media_id):  # noqa: E501
    """get_media_by_id

    Displays a media defined by the ID # noqa: E501

    :param media_id: codigo de la media
    :type media_id: int

    :rtype: Media
    """
    media = DBMedia.query.filter(DBMedia.id == media_id).first()

    if media == None:
        abort(404)
    return Media(media.id, media.media, media.link, media.title, media.size, media.duration, media.created, media.media_type, media.views, media.likes, media.owner_id, media.album_id)


@login_required
def save_media(body):  # noqa: E501
    """save_media

    Creates a media # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Media.from_dict(connexion.request.get_json())  # noqa: E501

        media = Media(
            media = body.media, 
            link = body.link, 
            title = body.title, 
            size = body.size, 
            duration = body.duration, 
            media_type = body.media_type, 
            views = body.views, 
            likes = body.likes,
            owner_id = body.owner_id,
            album_id = body.album_id
        )

        db.session.add(media)
        db.session.commit()

    return (Response(), 201)
