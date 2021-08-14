from flask import abort

from jobbing.DBModels import Country as DBCountry
from jobbing.DBModels import State as DBState
from jobbing.DBModels import Municipality as DBMunicipality
from jobbing.DBModels import Neighbourhood as DBNeighbourhood
from jobbing.DBModels import NotificationType as DBNotificationType
from jobbing.models.country import Country  # noqa: E501
from jobbing.models.municipality import Municipality  # noqa: E501
from jobbing.models.neighbourhood import Neighbourhood  # noqa: E501
from jobbing.models.notification_type import NotificationType  # noqa: E501
from jobbing.models.state import State  # noqa: E501


def get_countries():  # noqa: E501
    """get_countries

    Show a listing of neighbourhoods # noqa: E501


    :rtype: List[Country]
    """

    countries = DBCountry.query.all()
    if countries == None:
        abort(404)
    return [Country(c.id, c.name) for c in countries]


def get_country_by_id(country_id):  # noqa: E501
    """get_country_by_id

    Get country by id # noqa: E501

    :param country_id: Unique identifier
    :type country_id: str

    :rtype: Country
    """
    country = DBCountry.query.filter(DBCountry.id==country_id).first()
    if country == None:
        abort(404)
    return Country(country.id, country.name)


def get_municipalities_by_state_id(state_id):  # noqa: E501
    """get_municipalities_by_state_id

    Lists all municipalities of a state # noqa: E501

    :param state_id: Id of the state
    :type state_id: int

    :rtype: List[Municipality]
    """
    municipalities = DBMunicipality.query.filter(DBMunicipality.state_id==state_id)
    if municipalities == None:
        abort(404)
    return [Municipality(m.id, m.name, m.state_id) for m in municipalities]


def get_municipality_by_id(municipality_id):  # noqa: E501
    """get_municipality_by_id

    Get state by id # noqa: E501

    :param municipality_id: Unique identifier
    :type municipality_id: str

    :rtype: Municipality
    """
    munic = DBMunicipality.query.filter(DBMunicipality.id==municipality_id).first()
    if munic == None:
        abort(404)
    return Municipality(munic.id, munic.name, munic.state_id)


def get_neighbourhood_by_id(neighbourhood_id):  # noqa: E501
    """get_neighbourhood_by_id

    Get neighbourhood by id # noqa: E501

    :param neighbourhood_id: Unique identifier
    :type neighbourhood_id: str

    :rtype: Neighbourhood
    """
    neigh = DBNeighbourhood.query.filter(DBNeighbourhood.id==neighbourhood_id).first()
    if neigh == None:
        abort(404)
    return Neighbourhood(neigh.id, neigh.name, neigh.zip_code, neigh.municipality_id)


def get_neighbourhoods_by_municipality(municipality_id):  # noqa: E501
    """get_neighbourhoods_by_municipality

    Lists all neighbourhoods of a municipality # noqa: E501

    :param municipality_id: Id of the municipality
    :type municipality_id: int

    :rtype: List[Neighbourhood]
    """
    neigh = DBNeighbourhood.query.filter(DBNeighbourhood.municipality_id==municipality_id).first()
    if neigh == None:
        abort(404)
    return Neighbourhood(neigh.id, neigh.name, neigh.zip_code, neigh.municipality_id)


def get_notification_type_by_id(notificaction_type_id):  # noqa: E501
    """get_notification_type_by_id

    Shows a type of notification defined by the ID # noqa: E501

    :param notificaction_type_id: codigo del tipo de notificacion
    :type notificaction_type_id: int

    :rtype: NotificationType
    """
    type = DBNotificationType.query.filter(DBNotificationType.id==notificaction_type_id).first()
    if type == None:
        abort(404)
    return NotificationType(type.id, type.name)


def get_notification_types():  # noqa: E501
    """get_notification_types

    Show all types of notifications # noqa: E501


    :rtype: List[NotificationType]
    """
    types = DBNotificationType.query.all()
    if types == None:
        abort(404)
    return [NotificationType(t.id, t.name) for t in types]


def get_state_by_id(state_id):  # noqa: E501
    """get_state_by_id

    Get state by id # noqa: E501

    :param state_id: Unique identifier
    :type state_id: int

    :rtype: State
    """
    state = DBState.query.filter(DBState.id==state_id).first()
    if state == None:
        abort(404)
    return State(state.id, state.name, state.country_id)


def get_states_by_country_id(country_id):  # noqa: E501
    """get_states_by_country_id

    Lists all states of a country id # noqa: E501

    :param country_id: Name of the country
    :type country_id: int

    :rtype: List[State]
    """
    states = DBState.query.all()
    if states == None:
        abort(404)
    return [State(s.id, s.name, s.country_id) for s in states]
