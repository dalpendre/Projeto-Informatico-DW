import random
import sys
import psycopg2
from psycopg2 import Error

import constants


def insert_data_to_database(data):
    try:
        connection = psycopg2.connect(
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port,
            database=constants.db_name
        )

        cursor = connection.cursor()

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_road (road_name, road_type, road_length, number_of_lanes, start_point, end_point) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for record in data:
            values = (
                record['road_name'],
                record['road_type'],
                record['road_length'],
                record['number_of_lanes'],
                record['start_point'],
                record['end_point']
            )
            cursor.execute(insert_query, values)

        connection.commit()
        print("Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

class Road:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            generated_data[property_name] = self.generate_value(value_range)

        return generated_data

    @staticmethod
    def generate_value(value_range):
        value_type = value_range[0]

        if value_type == "int":
            min_value, max_value = value_range[1:]
            return random.randint(min_value, max_value)
        elif value_type == "float":
            min_value, max_value = value_range[1:]
            return random.uniform(min_value, max_value)
        elif value_type == "choice":
            choices = value_range[1:]
            return random.choice(choices)
        else:
            return None

    def generate_seeders(self, n):
        seeders = []
        for _ in range(n):
            seeder = Road(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])

property_ranges = {
    "road_name": ["choice", "...", "..."],
    "road_type": ["choice", "Highway/Expressway/Freeway", "Arterial Road", "Collector Road", "Local Street/Residential Street", "Rural Road", "Toll Road", "Parkways", "Motorway", "Freeway", "Autobahn", "Dual Carriageway", "Single Carriageway", "Interstate", "Cul-de-sac", "Alley", "Pedestrian Street", "Bicycle Lane/Cycle Track", "Bridge", "Tunnel", "Gravel Road", "Avenue", "Boulevard", "Court", "Drive", "Lane", "Parkway", "Road", "Street", "Way", "Access Road", "Frontage Road", "Service Road", "Crossroads", "Roundabout", "Overpass", "Underpass", "Flyover", "Bypass", "Causeway", "Viaduct", "Alleyway", "Boardwalk", "Promenade", "Terrace", "Greenway", "HOV Lane", "Bus Lane", "Shared-Use Path", "Scenic Byway", "Truck Route", "Ferry Road", "Farm Road", "Industrial Road", "Parking Lot/Car Park"],
    "road_length": ["int", 1, sys.maxsize],
    "number_of_lanes": ["int", 1, 100],
    "start_point": ["float", 1, sys.maxsize],
    "end_point" : ["float", 1, sys.maxsize],
}

# Create a Seeder instance
seeder = Road(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.insert_data_to_database()
    print(data)
    print("---")