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

        cursor.execute("SELECT MAX(road_sign_key) FROM t_road_sign")
        max_road_sign_key = cursor.fetchone()[0]
        if max_road_sign_key is None:
            max_road_sign_key = 0

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_road_sign (road_sign_key,road_sign_description,road_sign_code,road_sign_symbol,road_sign_class,road_sign_visibility) 
            VALUES (%s, %s, %s, %s, %s,%s)
        """

        # Generate new keys sequentially
        for record in data:
            max_road_sign_key += 1
            record['road_sign_key'] = max_road_sign_key

            values = (
                record['road_sign_key'],
                record['road_sign_description'],
                record['code'],
                record['symbol'],
                record['class_code'],
                record['visibility']
            )

            cursor.execute(insert_query, values)

        connection.commit()
        print("Road Sign Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
class RoadSign:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.curret_road_sign_key = property_ranges.get("road_sign_key", [])[1] - 1  # Initialize with the previous value


    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "road_sign_key":
                self.curret_road_sign_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.curret_road_sign_key
            else:
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
            seeder = RoadSign(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])

property_ranges = {
    "road_sign_key" : ["int", 1, sys.maxsize],
    "road_sign_description": ["choice", "Pedestrian Crossing Sign", "Parking Sign","No parking allowed sign","No U-Turn Sign","No Left Turn","No Entry Sign","Roundabout Sign","Give Way Sign"],
    "code" : ["choice","B1","B2","B3","B7","B9","B11","P","C11","C9"],
    "symbol": ["choice", "circle","inverted triangle","P","cross U", "cross Left","circle with line inside","people crossing"],
    "class_code" : ["int", 0, 100],
    "visibility": ["choice", "important", "high","medium","low"],
}

# Create a Seeder instance
seeder = RoadSign(property_ranges)

# Generate and print example data
for _ in range(1):
    seeder.insert_data_to_database()

"""
data = seeder.generate_random_data()
print(data)
print("---")
"""