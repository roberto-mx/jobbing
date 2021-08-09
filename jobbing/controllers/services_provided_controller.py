from flask import abort, Response
from flask_login import login_required
import connexion
import six

from jobbing.db import db
from jobbing.DBModels import ServiceProvided as DBServiceProvided
from jobbing.models.service_provided import ServiceProvided  # noqa: E501
from jobbing import util


@login_required
def get_service_provided_by_client_id(client_id):  # noqa: E501
    """get_service_provided_by_client_id

    Lists a service contracted by a specified client # noqa: E501

    :param client_id: Provided id
    :type client_id: int

    :rtype: ServiceProvided
    """
    serv = DBServiceProvided.query.filter(DBServiceProvided.client_id == client_id).first()

    if serv == None:
        abort(404)
    return ServiceProvided(
        id = serv.id,
        catalog_entries_id = serv.catalog_entries_id,
        client_id = serv.client_id,
        comment_entry = serv.comment_entry,
        created = serv.created,
        evaluation_id = serv.evaluation_id,
        last_updated = serv.last_updated,
        provider_id = serv.provider_id,
        rating = serv.rating,
        status = serv.status
    )


@login_required
def get_service_provided_by_id(service_provided_id):  # noqa: E501
    """get_service_provided_by_id

    Lists an evaluation defined by the ID # noqa: E501

    :param service_provided_id: Service Provided id
    :type service_provided_id: int

    :rtype: ServiceProvided
    """
    serv = DBServiceProvided.query.filter(DBServiceProvided.id == service_provided_id).first()

    if serv == None:
        abort(404)
    return ServiceProvided(
        id = serv.id,
        catalog_entries_id = serv.catalog_entries_id,
        client_id = serv.client_id,
        comment_entry = serv.comment_entry,
        created = serv.created,
        evaluation_id = serv.evaluation_id,
        last_updated = serv.last_updated,
        provider_id = serv.provider_id,
        rating = serv.rating,
        status = serv.status
    )


@login_required
def get_service_provided_by_provider_id(provider_id):  # noqa: E501
    """get_service_provided_by_provider_id

    Lists an service provided by a provided defined by id # noqa: E501

    :param provider_id: Provided id
    :type provider_id: int

    :rtype: ServiceProvided
    """
    serv = DBServiceProvided.query.filter(DBServiceProvided.provider_id == provider_id).first()

    if serv == None:
        abort(404)
    return ServiceProvided(
        id = serv.id,
        catalog_entries_id = serv.catalog_entries_id,
        client_id = serv.client_id,
        comment_entry = serv.comment_entry,
        created = serv.created,
        evaluation_id = serv.evaluation_id,
        last_updated = serv.last_updated,
        provider_id = serv.provider_id,
        rating = serv.rating,
        status = serv.status
    )


@login_required
def save_service_provided(body):  # noqa: E501
    """save_service_provided

    Creates a service provided entry # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = ServiceProvided.from_dict(connexion.request.get_json())  # noqa: E501

        serv = DBServiceProvided(
                catalog_entries_id = body.catalog_entries_id,
                client_id = body.client_id,
                comment_entry = body.comment_entry,
                created = body.created,
                evaluation_id = body.evaluation_id,
                last_updated = body.last_updated,
                provider_id = body.provider_id,
                rating = body.rating,
                status = body.status
        )

        db.session.add(serv)
        db.session.commit()

    return (Response(), 201)
