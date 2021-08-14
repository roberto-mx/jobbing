import jwt

from flask import current_app, request, jsonify
from flask_login import LoginManager
from functools import wraps


login_manager = LoginManager()


def init_login(app):
    login_manager.init_app(app)


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
            jwt.decode(token, current_app.secret_key, algorithms=["HS256"])
        except Exception as e:
            print(e)
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401

        return f(*args, **kwargs)
  
    return decorated