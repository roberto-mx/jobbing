from flask_seeder import Seeder
from jobbing.DBModels import Category


class DemoSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        print("seeding roles")
        default_categories = [Category(id=1, name="Oficios Generales", description="Oficios Generales", status="1"),
                         Category(id=2, name="Cuidado Personal", description="Cuidado Personal", status="1"),
                         Category(id=3, name="Automotriz", description="Automotriz", status="1"),
                         Category(id=4, name="Cuidado de Mascota", description="Cuidado de Mascota", status="1"),
                         Category(id=5, name="Limpieza", description="Limpieza", status="1"),
                         Category(id=6, name="Deportes", description="Deportes", status="1"),
                         Category(id=7, name="Eventos", description="Eventos", status="1"),
                         Category(id=8, name="Otros", description="Otros", status="1")]

        for role in default_roles:
            self.db.session.add(role)