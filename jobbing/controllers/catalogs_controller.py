import connexion
import six

from jobbing.models.country import Country  # noqa: E501
from jobbing.models.municipality import Municipality  # noqa: E501
from jobbing.models.neighborhood import Neighborhood  # noqa: E501
from jobbing.models.notification_type import NotificationType  # noqa: E501
from jobbing.models.state import State  # noqa: E501
from jobbing import util


def get_countries():  # noqa: E501
    """get_countries

    Show a listing of neighborhoods # noqa: E501


    :rtype: List[Country]
    """
    result = []
    result.append(Country(1, 'Mexico'))
    return result


def get_country_by_id(country_id):  # noqa: E501
    """get_country_by_id

    Get country by id # noqa: E501

    :param country_id: Unique identifier
    :type country_id: str

    :rtype: Country
    """
    result=Country(country_id)
    return 'do some magic!'


def get_municipalities_by_state_id(state_id):  # noqa: E501
    """get_municipalities_by_state_id

    Lists all municipalities of a state # noqa: E501

    :param state_id: Id of the state
    :type state_id: int

    :rtype: List[Municipality]
    """
    return 'do some magic!'


def get_municipality_by_id(municipality_id):  # noqa: E501
    """get_municipality_by_id

    Get state by id # noqa: E501

    :param municipality_id: Unique identifier
    :type municipality_id: str

    :rtype: Municipality
    """
    return 'do some magic!'


def get_neighborhood_by_id(neighborhood_id):  # noqa: E501
    """get_neighborhood_by_id

    Get neighborhood by id # noqa: E501

    :param neighborhood_id: Unique identifier
    :type neighborhood_id: str

    :rtype: Neighborhood
    """
    return 'do some magic!'


def get_neighborhoods_by_municipality(municipality_id):  # noqa: E501
    """get_neighborhoods_by_municipality

    Lists all neighborhoods of a municipality # noqa: E501

    :param municipality_id: Id of the municipality
    :type municipality_id: int

    :rtype: List[Neighborhood]
    """
    return 'do some magic!'


def get_notification_type_by_id(notificaction_type_id):  # noqa: E501
    """get_notification_type_by_id

    Shows a type of notification defined by the ID # noqa: E501

    :param notificaction_type_id: codigo del tipo de notificacion
    :type notificaction_type_id: int

    :rtype: NotificationType
    """
    return 'do some magic!'


def get_notification_types():  # noqa: E501
    """get_notification_types

    Show all types of notifications # noqa: E501


    :rtype: List[NotificationType]
    """
    return 'do some magic!'


def get_state_by_id(state_id):  # noqa: E501
    """get_state_by_id

    Get state by id # noqa: E501

    :param state_id: Unique identifier
    :type state_id: int

    :rtype: State
    """
    return 'do some magic!'


def get_states_by_country_id(country_id):  # noqa: E501
    """get_states_by_country_id

    Lists all states of a country id # noqa: E501

    :param country_id: Name of the country
    :type country_id: int

    :rtype: List[State]
    """
    return 'do some magic!'
