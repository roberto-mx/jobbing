from flask import abort, Response
import connexion

from jobbing.db import db
from jobbing.DBModels import Message as DBMessage
from jobbing.models.message import Message  # noqa: E501
from jobbing.login import token_required


@token_required
def get_message_by_id(message_id):  # noqa: E501
    """get_message_by_id

    List a messaged defined by message ID # noqa: E501

    :param message_id: codigo del mensaje
    :type message_id: int

    :rtype: Message
    """
    msg = DBMessage.query.filter(DBMessage.message_id == message_id).first()

    if msg == None:
        abort(404)

    return Message(
        id = msg.id,
        provider_id = msg.provider_id,
        service_id = msg.service_id,
        entry = msg.entry,
        status = msg.status,
        created = msg.created
    )


@token_required
def get_message_by_provider_id(provider_id):  # noqa: E501
    """get_message_by_provider_id

    Get all messages of a provider # noqa: E501

    :param provider_id: codigo del mensaje
    :type provider_id: int

    :rtype: Message
    """

    msg = DBMessage.query.filter(DBMessage.provider_id == provider_id).first()

    if msg == None:
        abort(404)

    return Message(
        id = msg.id,
        provider_id = msg.provider_id,
        service_id = msg.service_id,
        entry = msg.entry,
        status = msg.status,
        created = msg.created
    )


@token_required
def save_message(body):  # noqa: E501
    """save_message

    Creates a message for a provider # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
        
        msg = DBMessage(
            provider_id = body.provider_id,
            service_id = body.service_id,
            entry = body.entry,
            status = body.status
        )

        db.session.add(msg)
        db.session.commit()

    return (Response(), 201)
