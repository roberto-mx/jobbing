import connexion
import os

from flask import abort, Response, current_app, request
from werkzeug.utils import secure_filename

from jobbing.db import db
from jobbing.DBModels import Address as DBAddress
from jobbing.DBModels import User as DBUser
from jobbing.DBModels import Profile as DBProfile
from jobbing.models.address import Address  # noqa: E501
from jobbing.models.user_profile import UserProfile  # noqa: E501
from jobbing.login import token_required


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@token_required
def avatar_put(uid, body=None):  # noqa: E501
    """Upload an avatar

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request:

        user = DBUser.query.filter(DBUser.uid == uid).first()

        if user == None:
            abort(404)

        file = request.files['file']

        if body and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        
    return (Response(), 204)


@token_required
def get_addres_by_user_id(user_id):  # noqa: E501
    """get_addres_by_user_id

    Displays an Addres of a user # noqa: E501

    :param user_id: Unique identifier
    :type user_id: int

    :rtype: Address
    """
    address = DBAddress.query.filter(DBAddress.id == user_id).first()

    if address == None:
        abort(404)
    return Address(
        address_id = address.address_id,
        street = address.street,
        outer_number = address.outer_number,
        inner_number = address.inner_number,
        neighborhood_id = address.neighborhood_id,
        muncipality_id = address.muncipality_id,
        zip_code = address.zip_code,
        state_id = address.state_id,
    )


@token_required
def get_user_profile_by_id(uid):  # noqa: E501
    """get_user_profile_by_id

    Displays a User defined by ID # noqa: E501

    :param uid: Unique identifier
    :type uid: str

    :rtype: UserProfile
    """

    user = DBUser.query.filter(DBUser.uid== uid).first()

    if user == None:
        abort(404)

    profile = DBProfile.query.filter(DBProfile.id == user.id).first()

    if profile == None:
        abort(404)
    return UserProfile(
        userprofile_id=profile.id,
        first_name=profile.first_name,
        second_name=profile.second_name,
        first_surname=profile.first_surname,
        second_surname=profile.second_surname,
        birthdate=profile.birthdate,
        curp=profile.curp,
        mobile_number=profile.mobile_number,
        home_number=profile.home_number,
        office_number=profile.office_number,
        facebook_profile=profile.facebook_profile,
        linkedin_profile=profile.linkedin_profile,
        twitter_profile=profile.twitter_profile,
        id_image=profile.id_image,
        status=profile.status,
        created=profile.created,
        updated=profile.updated,
        # credentials_id=profile.credentials_id,
        # org_id = profile.org_id,
        address=profile.address
    )
    

@token_required
def save_address_profile(body):  # noqa: E501
    """save_address_profile

    Creates an address # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
        
        address = DBAddress(
            address_id=body.address_id,
            street=body.street,
            outer_number=body.outer_number,
            inner_number=body.inner_number,
            neighborhood_id=body.neighborhood_id,
            muncipality_id=body.muncipality_id,
            zip_code=body.zip_code,
            state_id=body.state_id
        )

        db.session.add(address)
        db.session.commit()

    return (Response(), 201)


@token_required
def save_user_profile(body):  # noqa: E501
    """save_user_profile

    Creates a user profile # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501

        profile = DBProfile(
                id=body.id,
                first_name=body.first_name,
                second_name=body.second_name,
                first_surname=body.first_surname,
                second_surname=body.second_surname,
                birthdate=body.birthdate,
                curp=body.curp,
                mobile_number=body.mobile_number,
                home_number=body.home_number,
                office_number=body.office_number,
                facebook_profile=body.facebook_profile,
                linkedin_profile=body.linkedin_profile,
                twitter_profile=body.twitter_profile,
                id_image=body.id_image,
                status=body.status,
                created=body.created,
                updated=body.updated,
                # credentials_id=body.credentials_id,
                # org_id = body.org_id,
                address=body.address
        )

        db.session.add(profile)
        db.session.commit()

    return (Response(), 201)


@token_required
def update_addres(body):  # noqa: E501
    """update_addres_by_user_id

    Updates a User attributes # noqa: E501

    :param user_id: Unique identifier
    :type user_id: int

    :rtype: Address
    """
    if connexion.request.is_json:
        body = Address.from_dict(connexion.request.get_json())  # noqa: E501

        address = DBAddress.query.filter(DBProfile.id == body.userprofile_id).first()

        address.address_id = body.address_id,
        address.street = body.street,
        address.outer_number = body.outer_number,
        address.inner_number = body.inner_number,
        address.neighborhood_id = body.neighborhood_id,
        address.muncipality_id = body.muncipality_id,
        address.zip_code = body.zip_code,
        address.state_id = body.state_id

        db.session.commit()

    return (Response(), 204)


@token_required
def update_user(body):  # noqa: E501
    """Update an existing user_profile

    :param body: UserProfile object that needs to be added to the store
    :type body: dict | bytes

    :rtype: UserProfile
    """
    if connexion.request.is_json:
        body = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501

        profile = DBProfile.query.filter(DBProfile.id == body.userprofile_id).first()

        profile.id = body.id,
        profile.first_name = body.first_name,
        profile.second_name = body.second_name,
        profile.first_surname = body.first_surname,
        profile.second_surname = body.second_surname,
        profile.birthdate = body.birthdate,
        profile.curp = body.curp,
        profile.mobile_number = body.mobile_number,
        profile.home_number = body.home_number,
        profile.office_number = body.office_number,
        profile.facebook_profile = body.facebook_profile,
        profile.linkedin_profile = body.linkedin_profile,
        profile.twitter_profile = body.twitter_profile,
        profile.id_image = body.id_image,
        profile.status = body.status,
        profile.created = body.created,
        profile.updated = body.updated,
        # profile.credentials_id = body.credentials_id,
        profile.org_id = body.org_id,
        profile.address = body.address

        db.session.commit()

    return (Response(), 204)
