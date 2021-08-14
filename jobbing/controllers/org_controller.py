from flask import abort, Response
from flask_login import login_required
import connexion

from jobbing.models.org import Org  # noqa: E501
from jobbing.db import db
from jobbing.DBModels import Org as DBOrg


def get_org_by_id(org_id):  # noqa: E501
    """get_org_by_id

    Displays an org # noqa: E501

    :param org_id: Unique identifier
    :type org_id: int

    :rtype: Org
    """
    org = DBOrg.query.filter(DBOrg.org_id == org_id).first()

    if org == None:
        abort(404)

    return Org(org_id=org.org_id, name=org.name, status=org.status)


def save_org(body):  # noqa: E501
    """save_org

    Creates a new org # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Org.from_dict(connexion.request.get_json())  # noqa: E501

        org = DBOrg(
            org_id = body.org_id,
            name = body.name, 
            status = body.status
        )

        db.session.add(org)
        db.session.commit()

    return (Response(), 201)
