from flask_seeder import Seeder
from jobbing.DBModels import Country, State, Municipality
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
        with open('../resources/states.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Skip header

            for row in csv_reader:
                state = State(id=int(row['CLAVE_ENTIDAD']), 
                            name=row['ENTIDAD_FEDERATIVA'],
                            country_id=mexico_id)
                self.db.session.add(state)

        print("seeding Catalogs->municipalities")
        with open('../resources/municipalities.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Skip header

            for row in csv_reader:
                municipality = Municipality(id=int(row['CLAVE_MUNICIPIO']), 
                                            name=row['MUNICIPIO'],
                                            state_id=int(row['CLAVE_ENTIDAD']))
                self.db.session.add()

