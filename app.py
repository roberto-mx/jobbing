#!/usr/bin/env python3

import connexion
import os

from flask_login import LoginManager

from jobbing import encoder
from jobbing import db
from jobbing import login

def database_uri():
    user = 'postgres'
    # pwd = os.environ['JOBBING_DB_PWD']
    pwd = 'BuronSuave03'
    host = 'localhost'
    port = '5432'
    name = 'postgres'

    return f'postgresql://{user}:{pwd}@{host}:{port}/{name}'

def main():
    app = connexion.FlaskApp(__name__, specification_dir='./jobbing/swagger')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={
                'title': 'Aprende tu mismo API'}, pythonic_params=True)
    app.app.config['SQLALCHEMY_DATABASE_URI'] = database_uri()
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
    app.app.config['UPLOAD_FOLDER'] = './'
    app.app.secret_key = 'iV+j6;|5C2<A&drOM*G:'
    app.debug = True

    db.load_db(app.app)
    login.init_login(app.app)

    return app.app


# It's required to be able to use 'Flask run'
application = main()


if __name__ == '__main__':
    application.run(port=8080, debug=True)
