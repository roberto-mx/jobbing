from flask_seeder import Seeder
import datetime
from jobbing.DBModels import Profile


class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 3

    def run(self):
        print("seeding profiles")
        default_profiles = [Profile(id=1,
                                 first_name='Admin',
                                 second_name='Admin',
                                 first_surname='Admin',
                                 second_surname='Admin',
                                 birthdate=datetime.datetime(1985, 1, 10),
                                 curp='XXXX851001XXXXXXXX',
                                 mobile_number='+523315487952',
                                 id_image='',
                                 status="active",
                                 address="admin address",
                                 user_id=1)]

        for profile in default_profiles:
            self.db.session.add(profile)

        self.db.session.commit()
