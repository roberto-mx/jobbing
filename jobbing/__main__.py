#!/usr/bin/env python3

import connexion

from jobbing import encoder
from flask_sqlalchemy import SQLAlchemy

from jobbing import db

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jce.sqlite3'
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.add_api('swagger.yaml', arguments={'title': 'Aprende tu mismo API'}, pythonic_params=True)
app.debug = True

# db = SQLAlchemy(app.app)

# with app.app.app_context():
#     db.create_all()

db.load_db(app.app)

app.run(port=8080)



