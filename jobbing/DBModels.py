from jobbing.db import get_db

db = get_db()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int = None, name: str = None, status: str = None):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self):
        return '<Role %r>' % self.name


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Country {self.name}>'


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    country_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int = None, name: str = None, country_id: str = None):
        self.id = id
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f'<State {self.name}>'


class Municipality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    state_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int = None, name: str = None, state_id: str = None):
        self.id = id
        self.name = name
        self.state_id = state_id

    def __repr__(self):
        return f'<Municipality {self.name}>'