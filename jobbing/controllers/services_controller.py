import connexion
import six

from jobbing.models.service import Service  # noqa: E501
from jobbing import util


def get_catalog_entry_by_id(service_id):  # noqa: E501
    """get_catalog_entry_by_id

    muestra una entrada de catalogo definida por el ID # noqa: E501

    :param service_id: codigo de la entrada del catalago
    :type service_id: int

    :rtype: Service
    """
    return 'do some magic!'


def get_services_by_catalog_id(catalog_id):  # noqa: E501
    """get_services_by_catalog_id

    Lists the media defined by mediaID # noqa: E501

    :param catalog_id: Catalog id
    :type catalog_id: int

    :rtype: Service
    """
    return 'do some magic!'


def save_service(body):  # noqa: E501
    """save_service

    Creates a media # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
