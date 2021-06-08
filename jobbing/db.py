from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def load_db(app):
    db.init_app(app)


def get_db():
    return db