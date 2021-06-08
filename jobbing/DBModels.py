from jobbing.db import get_db

db = get_db()

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.name