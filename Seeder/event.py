import random
import sys
import psycopg2
from psycopg2 import Error

import constants


def insert_data_to_database(data):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Erick2002@",
            host="localhost",
            port="5432",
            database="projeto_informatico_source_db"
        )

        cursor = connection.cursor()

        cursor.execute("SELECT MAX(event_key) FROM t_event")
        max_event_key = cursor.fetchone()[0]
        if max_event_key is None:
            max_event_key = 0

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_event (event_key,designation,start_time,end_time,flag_single_day_event) 
            VALUES (%s, %s, %s, %s, %s)
        """

        # Generate new keys sequentially
        for record in data:

                max_event_key += 1
                record['event_key'] = max_event_key

                values = (
                record['event_key'],
                record['designation'],
                record['start_time'],
                record['end_time'],
                record['flag_single_day_event']
            )

                cursor.execute(insert_query, values)

        connection.commit()
        print("Event Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

class Event:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_event_key = property_ranges.get("event_key", [])[1] - 1  # Initialize with the previous value


    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "event_key":
                self.current_event_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_event_key
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
        elif value_type == "boolean":
            return random.choice([True, False])
        else:
            return None

    def generate_seeders(self, n):
            seeders = []
            for _ in range(n):
                seeder = Event(self.property_ranges)
                seeders.append(seeder)
            return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])

property_ranges = {
    "event_key": ["int", 1, sys.maxsize],
    "designation": ["choice", "Car Race", "Car Rally","Car Cruise","Test Drive Event","Car Show"],
    "start_time": ["float", 1, sys.maxsize],
    "end_time": ["float", 1, sys.maxsize],
    "flag_single_day_event": ["boolean"],
}

# Create a Seeder instance
seeder = Event(property_ranges)

# Generate and print example data
for _ in range(3):
    seeder.insert_data_to_database()

"""
data = seeder.generate_random_data()
print(data)
print("---")
"""

