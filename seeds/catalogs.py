from flask_seeder import Seeder
from jobbing.DBModels import Country, State, Municipality, NotificationType, Neighbourhood
import csv


class CatalogsSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        mexico_id = 1

        print("seeding Catalogs->Country")
        self.db.session.add(Country(id=mexico_id, name="México"))

        print("seeding Catalogs->States")
        with open('resources/states.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader:
                state = State(id=int(row['CLAVE_ENTIDAD']), 
                            name=row['ENTIDAD_FEDERATIVA'],
                            country_id=mexico_id)
                self.db.session.add(state)

        print("seeding Catalogs->municipalities")
        with open('resources/municipalities.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            for row in csv_reader:
                municipality = Municipality(id=int(row['CLAVE_MUNICIPIO']), 
                                            name=row['MUNICIPIO'],
                                            state_id=int(row['CLAVE_ENTIDAD']))
                self.db.session.add(municipality)

        print("seeding Catalogs->Neihgbourhood")
        self.db.session.add(Neighbourhood(1, "Lomas Universidad", 45016, 120))
        self.db.session.add(Neighbourhood(2, "Chapalita las Fuentes", 45030, 120))
        self.db.session.add(Neighbourhood(3, "Ciudad Del Sol, 120", 45050, 120))
        self.db.session.add(Neighbourhood(4, "Ciudad Granja", 45010, 120))

        print("seeding Catalogs->NotificationType")
        self.db.session.add(NotificationType(1, "Mensaje"))


        print("Seeding Catalogs completed!")
