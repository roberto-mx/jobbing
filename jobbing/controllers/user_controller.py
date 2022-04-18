#!/usr/bin/env python
# -*- coding: utf-8 -*-
import connexion
import jwt

from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort, Response, make_response
from flask_login import logout_user, login_user
from flask import current_app, jsonify
from datetime import datetime, timedelta

from jobbing.db import db
from jobbing.DBModels import User as DBProfile
from jobbing.DBModels import User as DBUser
from jobbing.models.user import User  # noqa: E501
from jobbing.login import login_manager, token_required

# FIXME: Login Manager configured in remote mode
@login_manager.user_loader
def loader(user_id):
    user = DBUser.query.filter_by(id=user_id).first()
    return User(user_id=user.id, uid=user.uid, email=user.email, role_id=user.role_id), 200


def login(body):
    if not body or not body['email'] or not body['password']:
        # returns 401 if any email or / and password is missing
        return make_response('Could not verify', 401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )

    user = DBUser.query.filter_by(email=body['email']).first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response('Could not verify', 401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, body['password']):
        # generates the JWT Token
        token = jwt.encode({
            'uid': user.uid,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, current_app.secret_key, algorithm="HS256")

        login_user(user, remember=True)
  
        return make_response(jsonify({'token' : token}), 201)

    # returns 403 if password is wrong
    return make_response('Could not verify', 403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


@token_required
def logout():
    """Logout the current user."""

    logout_user()
    return 'logged out'


@token_required
def get_user_by_id(uid):  # noqa: E501
    """get_user_by_id

    Displays a User defined by ID # noqa: E501

    :param uid: Unique identifier
    :type uid: str

    :rtype: User
    """

    user = DBUser.query.filter(DBUser.uid == uid).first()

    if user == None:
        abort(404)
    return User(user_id=user.id, uid=user.uid, email=user.email, image_profile=user.image_profile, role_id=user.role_id)


@token_required
def get_users():  # noqa: E501
    """get_users

    Lists all users # noqa: E501


    :rtype: User
    """
    users = DBUser.query.all()
    results = [
        User(user_id=user.id, uid=user.uid, email=user.email, image_profile=user.image_profile, role_id=user.role_id) for user in users]
    return results


def signup(body):  # noqa: E501
    """save_user

    Creates a user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

        profile = DBProfile(
            id=body.profile.id,
            first_name=body.profile.first_name,
            second_name=body.profile.second_name,
            first_surname=body.profile.first_surname,
            second_surname=body.profile.second_surname,
            birthdate=body.profile.birthdate,
            curp=body.profile.curp,
            mobile_number=body.profile.mobile_number,
            home_number=body.profile.home_number,
            office_number=body.profile.office_number,
            facebook_profile=body.profile.facebook_profile,
            linkedin_profile=body.profile.linkedin_profile,
            twitter_profile=body.profile.twitter_profile,
            id_image=body.profile.id_image,
            status=body.profile.status,
            created=body.profile.created,
            updated=body.profile.updated,
            address=body.profile.address,
            user_id=body.profile.user_id
        )

        usr = DBUser(user_id=body.id,
                uid=body.uid,
                password=generate_password_hash(body.password),
                password_date=datetime.now(),
                email=body.email,
                image_profile=body.image_profile,
                role_id=body.role_id,
                profile=profile
        )

        db.session.add(usr)
        db.session.commit()

    return (Response(), 201)
