from flask_seeder import Seeder
from jobbing.DBModels import Album


class AlbumsSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        print("seeding albums")
        default_albums = [Album(id=1, title="IT Negocios", description="IT Negocios"),
                     Album(id=2, title="IT Basico", description="IT Basico"),
                     Album(id=3, title="Desarrollo personal y profesional", description="Desarrollo personal y profesional"),
                     Album(id=4, title="Marketing", description="Marketing"),
                     Album(id=5, title="Finanzas", description="Finanzas"),
                     Album(id=6, title="Comunicacion", description="Comunicacion")]    

        for album in default_albums:
            self.db.session.add(album)             