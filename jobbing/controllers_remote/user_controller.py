from flask import abort, make_response
from flask import current_app, jsonify
from flask_login import logout_user, login_user

from werkzeug.security import generate_password_hash, check_password_hash
import connexion
import jwt
from datetime import datetime, timedelta

from jobbing.login import login_manager, token_required

# DB Models
from jobbing.DBModelsRemote import UserModel as DBUserModel
from jobbing.DBModelsRemote import UserAuth as DBUserAuth
from jobbing.DBModelsRemote import UserAddress as DBUserAddress
from jobbing.DBModelsRemote import Media as DBMedia

# Swagger Models
from jobbing.models_remote.user_model import UserModel # noqa: E501
from jobbing.models_remote.user_auth import UserAuth # noqa: E501
from jobbing.models_remote.user_address import UserAddress # noqa: E501
from jobbing.models_remote.media import Media # noqa: E501


"""
GET /users
"""
@token_required
def get_users(): # noqa: E501
    """get_users

    Show a listing of users # noqa: E501

    :rtype: List[UserModel]
    """
    
    users = DBUserModel.query.all()
    if users == None:
        abort(404)
    return [UserModel(
        u.user_model_id, 
        u.user_status_id, 
        u.user_role_id, 
        u.user_model_first_name, 
        u.user_model_last_name, 
        u.user_model_surname, 
        u.user_model_birthday, 
        u.user_model_phone_number, 
        u.user_model_address_id, 
        u.user_skills_id, 
        u.user_model_registry_date, 
        u.user_model_updated_date, 
        u.user_model_media_id) for u in users]

"""
GET /users/:id
"""
@token_required
def get_user_by_id(user_model_id): # noqa: E501
    """get_user_by_id

    Get user by id # noqa: E501

    :rtype: UserModel
    """

    u = DBUserModel.query.filter(DBUserModel.user_model_id == user_model_id).first()
    if u == None:
        abort(404)
    return UserModel(
        u.user_model_id, 
        u.user_status_id, 
        u.user_role_id, 
        u.user_model_first_name, 
        u.user_model_last_name, 
        u.user_model_surname, 
        u.user_model_birthday, 
        u.user_model_phone_number, 
        u.user_model_address_id, 
        u.user_skills_id, 
        u.user_model_registry_date, 
        u.user_model_updated_date, 
        u.user_model_media_id)

"""
GET /users/:id/auth
"""
@token_required
def get_user_auth_by_id(user_model_id): # noqa: E501
    """get_user_auth_by_id

    Get user auth info by id # noqa: E501

    :rtype: UserAuth
    """
    
    auth = DBUserAuth.query.filter(DBUserAuth.user_model_id == user_model_id).first()
    if auth == None:
        abort(404)
    return UserAuth(
        auth.user_auth_id, 
        auth.user_auth_password, 
        auth.user_auth_pass_date, 
        auth.user_model_id, 
        auth.user_auth_updated_date, 
        auth.user_auth_name)

"""
GET /users/:id/address
"""
@token_required
def get_user_address_by_id(user_model_id): # noqa: E501
    """get_user_address_by_id

    Get user address info by id # noqa: E501

    :rtype: UserAddress
    """

    user_model = DBUserModel.query.filter(DBUserModel.user_model_id == user_model_id).first()
    if user_model == None:
        abort(404)
    address = DBUserAddress.query.filter(DBUserAddress.id_user_address == user_model.user_model_address_id).first()
    if address == None:
        abort(404)
    return UserAddress(address.id_user_address, 
        address.street_name, 
        address.main_number, 
        address.interior_number, 
        address.id_colony_code, 
        address.id_zip_code, 
        address.id_state_code, 
        address.id_municipality, 
        address.id_country_code, 
        address.date_added, 
        address.last_update_date)

"""
GET users/:id/media
"""
@token_required
def get_user_media_by_id(user_model_id): # noqa: E501
    """get_user_address_by_id

    Get user media info by id (profile picture) # noqa: E501

    :rtype: Media
    """
    user_model = DBUserModel.query.filter(DBUserModel.user_model_id == user_model_id).first()
    if user_model == None:
        abort(404)
    media = DBMedia.query.filter(DBMedia.media_id == user_model.user_model_media_id).first()
    if media == None:
        abort(404)
    return Media(media.media_id, 
        media.media_status_id, 
        media.media_data.decode("utf-8"), 
        media.media_link, 
        media.media_title, 
        media.media_description, 
        media.media_size, 
        media.media_content_upload_date, 
        media.media_content_updated_date)

"""
GET /users/filter

params:
user_rol_id: int
status_id: int
skills_id: int
"""
@token_required
def get_users_with_filter(user_role_id=None, status_id=None, skills_id=None): # noqa: E501
    """get_users_with_filter

    Get users with filter # noqa: E501

    :rtype: List[UserModel]
    """
    users = DBUserModel.query.filter(
        (DBUserModel.user_role_id == user_role_id if user_role_id is not None else True), 
        (DBUserModel.user_status_id == status_id if status_id is not None else True), 
        (DBUserModel.user_skills_id == skills_id if skills_id is not None else True))

    if users == None:
        abort(404)
    return [UserModel(
        u.user_model_id, 
        u.user_status_id, 
        u.user_role_id, 
        u.user_model_first_name, 
        u.user_model_last_name, 
        u.user_model_surname, 
        u.user_model_birthday, 
        u.user_model_phone_number, 
        u.user_model_address_id, 
        u.user_skills_id, 
        u.user_model_registry_date, 
        u.user_model_updated_date, 
        u.user_model_media_id) for u in users]

"""
POST /login 
"""
def login(body): # noqa: E501
    if not body or not body["user_auth_name"] or not body["user_auth_password"]:
        # returns 401 if any email or / and password is missing
        return make_response('Could not verify', 401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )

    user = DBUserAuth.query.filter(DBUserAuth.user_auth_name == body["user_auth_name"]).first()
    if not user:
        # returns 401 if user does not exist
        return make_response('Could not verify', 401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )

    if check_password_hash(user.user_auth_password, body['user_auth_password']):
        # generates the JWT Token
        token = jwt.encode({
            'uid': user.user_auth_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, current_app.secret_key, algorithm="HS256")

        # FIXME: flask login session
        # login_user(user, remember=True)

        return make_response(jsonify({'token' : token}), 201)

# TODO: erase hasher
@token_required
def get_hash(param): # noqa: E501
    return make_response(jsonify({'hashed': generate_password_hash(param)}), 201)