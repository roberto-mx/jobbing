#!/usr/bin/env python3

import connexion

from jobbing import encoder


app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Aprende tu mismo API'}, pythonic_params=True)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jce.sqlite3'
app.debug = True

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Aprende tu mismo API'}, pythonic_params=True)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jce.sqlite3'
    app.debug = True

    return app


if __name__ == '__main__':
    main().run(port=8080)
