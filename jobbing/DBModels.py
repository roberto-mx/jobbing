import uuid
from datetime import date
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from jobbing.db import get_db

db = get_db()


class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    user = db.relationship("user")

    def __init__(self, id: int = None, name: str = None, status: str = None):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    password_date = db.Column(db.Date)
    email = db.Column(db.String(150), unique=True, nullable=False)
    image_profile = db.Column(db.String(2500), unique=False, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    profile = db.relationship("profile")

    def __init__(self, id: int = None, username: str = None, password: str = None, email: str = None, image_profile: str = None, role_id: int = None):
        self.id = id
        self.uid = str(uuid.uuid4())
        self.username = username
        self.password = generate_password_hash(password)
        self.password_date = date.today()
        self.email = email
        self.image_profile = image_profile
        self.role_id = role_id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {id}, {username}, {email}>'.format(**self)


class Profile(UserMixin, db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(150), nullable=False)
    second_name = db.Column(db.String(150), nullable=False)
    first_surname = db.Column(db.String(150), nullable=False)
    second_surname = db.Column(db.String(150), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    curp = db.Column(db.String(18), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    home_number = db.Column(db.String(15), nullable=True)
    office_number = db.Column(db.String(15), nullable=True)
    facebook_profile = db.Column(db.String(150), nullable=True)
    linkedin_profile = db.Column(db.String(150), nullable=True)
    twitter_profile = db.Column(db.String(150), nullable=True)
    id_image = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Enum('active', 'suspended'), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    # credentials_id = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    # org_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,
                 id: int = None,
                 first_name: str = None,
                 second_name: str = None,
                 first_surname: str = None,
                 second_surname: str = None,
                 birthdate: str = None,
                 curp: str = None,
                 mobile_number: str = None,
                 home_number: str = None,
                 office_number: str = None,
                 facebook_profile: str = None,
                 linkedin_profile: str = None,
                 twitter_profile: str = None,
                 id_image: str = None,
                 status: str = None,
                 credentials_id: str = None,
                 address: str = None,
                 org_id: str = None,
                 user_id: int = None):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.first_surname = first_surname
        self.second_surname = second_surname
        self.birthdate = birthdate
        self.curp = curp
        self.mobile_number = mobile_number
        self.home_number = home_number
        self.office_number = office_number
        self.facebook_profile = facebook_profile
        self.linkedin_profile = linkedin_profile
        self.twitter_profile = twitter_profile
        self.id_image = id_image
        self.status = status
        self.created = date.today()
        self.updated = date.today()
        self.address = address
        self.org_id = org_id
        self.user_id = user_id

    def __repr__(self):
        return '<Profile id={id}, first_name={first_name}, first_surname={last_name}, user_id={user_id}>'.format(**self)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int = None, name: str = None, description: str = None, status: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.status = status

    def __repr__(self):
        return '<Category %r>' % self.name
