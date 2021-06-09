from flask_seeder import Seeder
from jobbing.DBModels import Role
# from SQK


class DemoSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        print("seeding roles")
        default_roles = [Role(id=1, name="Admin", status="1"),
                         Role(id=2, name="Client", status="1"),
                         Role(id=3, name="Provider", status="1")]

        for role in default_roles:
            print(role)
            self.db.session.add(role)
