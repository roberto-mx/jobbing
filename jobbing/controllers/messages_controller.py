import connexion
import six

from jobbing.models.message import Message  # noqa: E501
from jobbing import util


def get_message_by_id(message_id):  # noqa: E501
    """get_message_by_id

    List a messaged defined by message ID # noqa: E501

    :param message_id: codigo del mensaje
    :type message_id: int

    :rtype: Message
    """
    return 'do some magic!'


def get_message_by_provider_id(provider_id):  # noqa: E501
    """get_message_by_provider_id

    Get all messages of a provider # noqa: E501

    :param provider_id: codigo del mensaje
    :type provider_id: int

    :rtype: Message
    """
    return 'do some magic!'


def save_message(body):  # noqa: E501
    """save_message

    Creates a message for a provider # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Message.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
