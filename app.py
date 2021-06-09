#!/usr/bin/env python3

import connexion

from jobbing import encoder
from jobbing import db


def main():
    app = connexion.FlaskApp(__name__, specification_dir='./jobbing/swagger')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={
                'title': 'Aprende tu mismo API'}, pythonic_params=True)
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jce.sqlite3'
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.debug = True

    db.load_db(app.app)

    return app.app


# It's required to be able to use 'Flask run'
application = main()

if __name__ == '__main__':
    application.run(port=8080, debug=True)
