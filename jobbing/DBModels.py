import uuid
from datetime import date
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from jobbing.db import db


class Address(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(80))
    outer_number = db.Column(db.String(10))
    inner_number = db.Column(db.String(10))
    neighborhood_id = db.Column(db.Integer)
    muncipality_id = db.Column(db.Integer)
    zip_code = db.Column(db.String(80))
    state_id = db.Column(db.Integer)

    def __init__(self, id: int=None,
            street: str=None,
            outer_number: str=None,
            inner_number: str=None,
            neighborhood_id: int=None,
            muncipality_id: int=None,
            zip_code: int=None,
            state_id: int=None):
        self.id = id
        self.street = street
        self.outer_number = outer_number
        self.inner_number = inner_number
        self.neighborhood_id = neighborhood_id
        self.muncipality_id = muncipality_id
        self.zip_code = zip_code
        self.state_id = state_id

    def __repr__(self):
        return '<Address {id}, {street}, {outer_number}, {inner_number}, {neighborhood_id}, {muncipality_id}, {zip_code}, {state_id}>'.format(**self)


class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    user = db.relationship("User")

    def __init__(self, id: int = None, name: str = None, status: str = None):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self):
        return '<Role %r>' % self.name


class Country(db.Model):
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Country {self.name}>'


class State(db.Model):
    __tablename__ = "state"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    country_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int=None, name: str=None, country_id: str=None):
        self.id = id
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f'<State {self.name}>'


# class Municipality(db.Model):
#     __tablename__ = "municipality"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     state_id = db.Column(db.Integer, nullable=False, primary_key=True)

#     def __init__(self, id: int=None, name: str=None, state_id: str=None):
#         self.id = id
#         self.name = name
#         self.state_id = state_id

#     def __repr__(self):
#         return f'<Municipality {self.name}>'


class Neighbourhood(db.Model):
    __tablename__ = "neighbourhood"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    zip_code = db.Column(db.Integer)
    municipality_id = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int=None, name: str=None, zip_code: int=None, municipality_id: int=None):
        self.id = id
        self.name = name
        self.zip_code = zip_code
        self.municipality_id = municipality_id

    def __repr__(self):
        return '<Neighbourhood {id}, {name}, {zip_code}, {municipality_id}>'.format(**self)


class NotificationType(db.Model):
    __tablename__ = "notification_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)

    def __init__(self, id: int=None, name: str=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<NotificationType {self.name}>'


# class Org(db.Model):
#     __tablename__ = "org"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     status = db.Column(db.Integer)

#     def __init__(self, id: int=None, name: str=None, status: int=None):
#         self.id = id
#         self.name = name
#         self.status = status

#     def __repr__(self):
#         return '<Org {id}, {name}, {status}>'.format(**self)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    password_date = db.Column(db.Date)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    profile = db.relationship("Profile")

    def __init__(self, id: int = None, password: str = None, email: str = None, image_profile: str = None, role_id: int = None):
        self.id = id
        self.uid = str(uuid.uuid4())
        self.password = generate_password_hash(password)
        self.password_date = date.today()
        self.email = email
        self.role_id = role_id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {uid}, {email}, {role_id}>'.format(**self)


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
    image_profile = db.Column(db.String(150), nullable=False)
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
                 image_profile: str = None,
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
        self.image_profile = image_profile
        self.status = status
        self.credentials_id = credentials_id,
        self.created = date.today()
        self.updated = date.today()
        self.address = address
        self.org_id = org_id
        self.user_id = user_id

    def __repr__(self):
        return '<Profile id={id}, first_name={first_name}, first_surname={last_name}, user_id={user_id}>'.format(**self)


class Category(db.Model):
    __tablename__ = "category"

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

class Skill(db.Model):
    __tablename__ = "skill"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    years_of_experience = db.Column(db.Integer, nullable=False)
    price_of_service = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500))
    work_zone = db.Column(db.String(100), nullable=False)
    services_provided = db.Column(db.Integer)
    five_stars = db.Column(db.Integer)
    four_starts = db.Column(db.Integer)
    three_starts = db.Column(db.Integer)
    two_starts = db.Column(db.Integer)
    one_start = db.Column(db.Integer)

    def __init__(self, id: int=None, category_id: int=None, 
            years_of_experience: float=None, price_of_service: int=None,
            description: str=None, work_zone: str=None,
            services_provided: int=None, five_stars: int=None,
            four_starts: int=None, three_starts: int=None,
            two_starts: int=None, one_start: int=None):
        self.id = id
        self.category_id = category_id
        self.years_of_experience = years_of_experience
        self.price_of_service = price_of_service
        self.description = description
        self.work_zone = work_zone
        self.services_provided=services_provided
        self.five_stars=five_stars
        self.four_starts=four_starts
        self.three_starts=three_starts
        self.two_starts=two_starts
        self.one_start=one_start

    def __repr__(self):
        return '<Skill {id}, {category_id}, {years_of_experience}, {price_of_service}, {description}, {work_zone}, {services_provided}, {five_stars}, {four_starts}, {three_starts}, {two_starts}, {one_starts}>'.format(**self)



class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)
    price_of_service = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500))
    work_zone = db.Column(db.String(100), nullable=False)
    services_provided = db.Column(db.Integer)
    five_stars = db.Column(db.Integer)
    four_starts = db.Column(db.Integer)
    three_starts = db.Column(db.Integer)
    two_starts = db.Column(db.Integer)
    one_start = db.Column(db.Integer)
    created = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    read_only = db.Column(db.Boolean)
    last_updated = db.Column(db.DateTime, nullable=True)
    status_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, 
            id: int=None,
            category_id: int=None,
            years_of_experience: float=None,
            price_of_service: int=None,
            description: str=None,
            work_zone: str=None,
            services_provided: int=None,
            five_stars: int=None,
            four_starts: int=None,
            three_starts: int=None,
            two_starts: int=None,
            one_start: int=None,
            created: db.DateTime=None,
            read_only: db.Boolean=None,
            last_updated: db.DateTime=None,
            status_id: int=None,
            user_id: int=None):

        self.id = id
        self.category_id = category_id
        self.years_of_experience = years_of_experience
        self.price_of_service = price_of_service
        self.description = description
        self.work_zone = work_zone
        self.services_provided=services_provided
        self.five_stars=five_stars
        self.four_starts=four_starts
        self.three_starts=three_starts
        self.two_starts=two_starts
        self.one_start=one_start
        self.created = created
        self.read_only = read_only
        self.last_updated = last_updated
        self.status_id = status_id
        self.user_id = user_id

    def __repr__(self):
        return '<Service {id}, {category_id}, {years_of_experience}, {price_of_service},'\
            ' {description}, {work_zone}, {services_provided}, {five_stars}, {four_starts},'\
            ' {three_starts}, {two_starts}, {one_starts}, {created}, {read_only},'\
            ' {last_updated}, {status_id}, {user_id}>'.format(**self)


class ServiceProvided(db.Model):
    __tablename__ = "service_provided"

    id = db.Column(db.Integer, primary_key=True)
    catalog_entries_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer, nullable=False)
    comment_entry = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    evaluation_id = db.Column(db.Integer)
    last_updated = db.Column(db.DateTime)
    provider_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int=None, catalog_entries_id: int=None, 
            client_id: int=None, comment_entry: int=None, created: int=None, 
            evaluation_id: int=None, last_updated: int=None, 
            provider_id: int=None, rating: int=None, status: int=None):
        self.id = id
        self.catalog_entries_id = catalog_entries_id
        self.client_id = client_id
        self.comment_entry = comment_entry
        self.created = created
        self.evaluation_id = evaluation_id
        self.last_updated = last_updated
        self.provider_id = provider_id
        self.rating = rating
        self.status = status

    def __repr__(self):
        return '<Service {catalog_entries_id}, {client_id}, {comment_entry}, '\
                '{created}, {evaluation_id}, {last_updated}, {provider_id}, '\
                '{rating}, {status}>'.format(**self)


class Notification(db.Model):
    __tablename__ = "notification"

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    media_id = db.Column(db.Integer)
    message = db.Column(db.String(255))
    notification_type_id = db.Column(db.Integer, db.ForeignKey('notification_type.id'))
    status = db.Column(db.Integer)
    title = db.Column(db.String(80))
    updated = db.Column(db.DateTime)

    def __init__(self, id: int=None, account_id: int=None, created: int=None, 
            media_id: int=None, message: int=None, notification_type_id: int=None,
            status: int=None, title: int=None, updated: int=None):
        self.id = id
        self.account_id = account_id
        self.created = created
        self.media_id = media_id
        self.message = message
        self.notification_type_id = notification_type_id
        self.status = status
        self.title = title
        self.updated = updated

    def __repr__(self):
        return '<Service {id}, {account_id}, {created}, {media_id}, {message}, '\
                '{notification_type_id}, {status}, {title}, {updated}>'.format(**self)


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    entry = db.Column(db.String(500), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, id, provider_id, service_id, entry, status):
        self.id = id
        self.provider_id = provider_id
        self.service_id = service_id
        self.entry = entry
        self.status = status

    def __repr__(self):
        return '<Service {id}, {provider_id}, {service_id}, '\
                '{entry}, {status}, {created}>'.format(**self)

class Album(db.Model):
    __tablename__ = "album"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, id: int = None, title: str = None, description: str = None):
        self.id = id
        self.title = title
        self.description = description    

    def __repr__(self):
        return '<Album %r>' % self.title    

# class Media(db.Model):
#     __tablename__ = "media"

#     id = db.Column(db.Integer, primary_key=True)
#     media = db.Column(db.String(80), unique=True, nullable=True)
#     link = db.Column(db.String(100), nullable=False)
#     title = db.Column(db.String(80), unique=False, nullable=False)
#     size = db.Column(db.Integer, nullable=True)
#     duration = db.Column(db.String(100), nullable=False)
#     created = db.Column(db.DateTime, nullable=False)
#     media_type = db.Column(db.String(100), nullable=False)
#     views = db.Column(db.Integer, nullable=False)
#     likes = db.Column(db.Integer, nullable=False)
#     owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     album_id = db.Column(db.Integer, nullable=False)

#     def __init__(self, id: int = None, 
#                  media: str = None, 
#                  link: str = None, 
#                  title: str = None, 
#                  size: int = None, 
#                  duration: str = None, 
#                  created: str = None,
#                  media_type: str = None,
#                  views: int = None,
#                  likes: int = None,
#                  owner_id: int = None,
#                  album_id: int = None ):
#         self.id = id
#         self.media = media  
#         self.link = link  
#         self.title = title
#         self.size = size
#         self.duration = duration  
#         self.created = created
#         self.media_type = media_type
#         self.views = views
#         self.likes = likes
#         self.owner_id = owner_id
#         self.album_id = album_id

#     def __repr__(self):
#         return '<Media %r>' % self.title
