from flask_seeder import Seeder
from jobbing.DBModels import Role


class RoleSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    def run(self):

        print("Removing default roles")
        role_ids = [1, 2, 3]

        for id in role_ids:
            self.db.session.remove()

        print("seeding roles")
        default_roles = [Role(id=1, name="Admin", status="1"),
                         Role(id=2, name="Client", status="1"),
                         Role(id=3, name="Provider", status="1")]

        for role in default_roles:
            self.db.session.add(role)

        self.db.session.commit()
