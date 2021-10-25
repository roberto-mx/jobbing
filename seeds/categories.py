from flask_seeder import Seeder
from jobbing.DBModels import Category


class CategoriesSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        print("seeding categories")
        default_categories = [
                Category(id=1, name="Oficios Generales", description="Oficios Generales", status="1"),
                Category(id=2, name="Servicios del hogar", description="Servicios del hogar", status="1"),
                Category(id=3, name="Cuidado Personal", description="Cuidado Personal", status="1"),
                Category(id=4, name="Automotriz", description="Automotriz", status="1"),
                Category(id=5, name="Cuidado de Mascota", description="Cuidado de Mascota", status="1"),
                Category(id=6, name="Limpieza", description="Limpieza", status="1"),
                Category(id=7, name="Deportes", description="Deportes", status="1"),
                Category(id=8, name="Eventos", description="Eventos", status="1"),
                Category(id=9, name="Transporte", description="Transporte", status="1"),
                Category(id=10, name="Otros", description="Otros", status="1")
        ]

        for category in default_categories:
            self.db.session.add(category)