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
        description = serv.description,
        years_of_experience = serv.years_of_experience,
        price_of_service = serv.price_of_service,
        work_zone = serv.work_zone,
        services_provided = serv.services_provided,
        five_stars = serv.five_stars,
        four_starts = serv.four_starts,
        three_starts = serv.three_starts,
        two_starts = serv.two_starts,
        one_start = serv.one_start,
        created = serv.created,
        read_only = serv.read_only,
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
        description = serv.description,
        years_of_experience = serv.years_of_experience,
        price_of_service = serv.price_of_service,
        work_zone = serv.work_zone,
        services_provided = serv.services_provided,
        five_stars = serv.five_stars,
        four_starts = serv.four_starts,
        three_starts = serv.three_starts,
        two_starts = serv.two_starts,
        one_start = serv.one_start,
        created = serv.created,
        read_only = serv.read_only,
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
        serv = Service.from_dict(connexion.request.get_json())  # noqa: E501

        service = Service(
            category_id = serv.category_id,
            description = serv.description,
            years_of_experience = serv.years_of_experience,
            price_of_service = serv.price_of_service,
            work_zone = serv.work_zone,
            services_provided = serv.services_provided,
            five_stars = serv.five_stars,
            four_starts = serv.four_starts,
            three_starts = serv.three_starts,
            two_starts = serv.two_starts,
            one_start = serv.one_start,
            read_only = serv.read_only,
            status_id = serv.status_id,
            user_id = serv.user_id
        )

        db.session.add(service)
        db.session.commit()

    return (Response(), 201)
