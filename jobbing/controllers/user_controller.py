#!/usr/bin/env python
# -*- coding: utf-8 -*-
import connexion
import six

from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort, request, Response, make_response
from flask_login import logout_user, login_required, login_user, LoginManager
from flask import current_app

from flask import jsonify
import jwt
from datetime import datetime, timedelta
from functools import wraps

from jobbing.DBModels import User as DBUser
from jobbing.models.user import User  # noqa: E501
from jobbing.login import login_manager
from jobbing import util


@login_manager.user_loader
def loader(body):
    user = body['username']
    pwd = body['password']
    user = DBUser.query.filter_by(username=user).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, pwd):
        return None

    return User(user_id=user.id, uid=user.uid, username=user.username, email=user.email, image_profile=user.image_profile, role_id=user.role_id), 200


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, current_app.secret_key, algorithms=["HS256"])
            current_user = DBUser.query.filter_by(uid = data.get('uid')).first()
        except Exception as e:
            print(e)
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401

        user = User(user_id=current_user.id, uid=current_user.uid, 
                username=current_user.username, email=current_user.email, 
                image_profile=current_user.image_profile, 
                role_id=current_user.role_id)
        # returns the current logged in users contex to the routes
        #return  f(user, *args, **kwargs)
        return  f(*args, **kwargs)
  
    return decorated


def login(body):
    
    if not body or not body['username'] or not body['password']:
        # returns 401 if any email or / and password is missing
        return make_response('Could not verify', 401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )

    user = DBUser.query.filter_by(username=body['username']).first()
  
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
        print("TOKEN:", token)

        login_user(user, remember=True)
  
        return make_response(jsonify({'token' : token}), 201)

    # returns 403 if password is wrong
    return make_response('Could not verify', 403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


@login_required
def logout():
    """Logout the current user."""
    #user = current_user
    #user.authenticated = False
    #db.session.add(user)
    #db.session.commit()
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
    return User(user_id=user.id, uid=user.uid, username=user.username, email=user.email, image_profile=user.image_profile, role_id=user.role_id)

@login_required
def get_users():  # noqa: E501
    """get_users

    Lists all users # noqa: E501


    :rtype: User
    """
    users = DBUser.query.all()
    results = [
        User(user_id=user.id, uid=user.uid, username=user.username, email=user.email, image_profile=user.image_profile, role_id=user.role_id) for user in users]
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
    return 'do some magic!'
