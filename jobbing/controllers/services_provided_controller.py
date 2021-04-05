import connexion
import six

from jobbing.models.service_provided import ServiceProvided  # noqa: E501
from jobbing import util


def get_service_provided_by_client_id(client_id):  # noqa: E501
    """get_service_provided_by_client_id

    Lists a service contracted by a specified client # noqa: E501

    :param client_id: Provided id
    :type client_id: int

    :rtype: ServiceProvided
    """
    return 'do some magic!'


def get_service_provided_by_id(service_provided_id):  # noqa: E501
    """get_service_provided_by_id

    Lists an evaluation defined by the ID # noqa: E501

    :param service_provided_id: Service Provided id
    :type service_provided_id: int

    :rtype: ServiceProvided
    """
    return 'do some magic!'


def get_service_provided_by_provider_id(provider_id):  # noqa: E501
    """get_service_provided_by_provider_id

    Lists an service provided by a provided defined by id # noqa: E501

    :param provider_id: Provided id
    :type provider_id: int

    :rtype: ServiceProvided
    """
    return 'do some magic!'


def save_service_provided(body):  # noqa: E501
    """save_service_provided

    Creates a service provided entry # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = ServiceProvided.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
