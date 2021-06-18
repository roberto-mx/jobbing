from flask_seeder import Seeder
from jobbing.DBModels import User


class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 2

    def run(self):
        print("seeding users")
        default_users = [User(1, 'admin', 'admin', 'admin@admin.com', "", 1)]

        for user in default_users:
            self.db.session.add(user)

        self.db.session.commit()
