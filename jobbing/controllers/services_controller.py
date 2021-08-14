from flask import abort, Response
import connexion

from jobbing.db import db
from jobbing.DBModels import Service as DBService
from jobbing.models.service import Service  # noqa: E501
from jobbing.login import token_required


@token_required
def get_catalog_entry_by_id(service_id):  # noqa: E501
    """get_catalog_entry_by_id

    muestra una entrada de catalogo definida por el ID # noqa: E501

    :param service_id: codigo de la entrada del catalago
    :type service_id: int

    :rtype: Service
    """
    serv = DBService.query.filter(DBService.service_id == service_id).first()

    if serv == None:
        abort(404)

    return DBService(
        id = serv.id,
        category_id = serv.category_id,
        cost = serv.cost,
        created = serv.created,
        read_only = serv.read_only,
        description = serv.description,
        last_updated = serv.last_updated,
        status_id = serv.status_id,
        user_id = serv.user_id
    )


@token_required
def get_services_by_catalog_id(catalog_id):  # noqa: E501
    """get_services_by_catalog_id

    Lists the media defined by mediaID # noqa: E501

    :param catalog_id: Catalog id
    :type catalog_id: int

    :rtype: Service
    """
    serv = DBService.query.filter(DBService.category_id == catalog_id).first()

    if serv == None:
        abort(404)

    return DBService(
        id = serv.id,
        category_id = serv.category_id,
        cost = serv.cost,
        created = serv.created,
        read_only = serv.read_only,
        description = serv.description,
        last_updated = serv.last_updated,
        status_id = serv.status_id,
        user_id = serv.user_id
    )


@token_required
def save_service(body):  # noqa: E501
    """save_service

    Creates a media # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501

        service = Service(
            category_id = body.category_id,
            cost = body.cost,
            read_only = body.read_only,
            description = body.description,
            status_id = body.status_id,
            user_id = body.user_id
        )

        db.session.add(service)
        db.session.commit()

    return (Response(), 201)
