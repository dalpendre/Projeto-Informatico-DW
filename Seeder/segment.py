import random
import sys
import psycopg2
from psycopg2 import Error

import constants

def insert_data_to_database(data, road_key):
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
            INSERT INTO t_segment (road_key,segment_name,segment_type,segment_length,number_of_lanes,start_point,end_point)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        for record in data:
            values = (
               road_key,
                record['segment_name'],
                record['segment_type'],
                record['segment_length'],
                record['number_of_lanes'],
                record['start_point'],
                record['end_point']
            )
            cursor.execute(insert_query, values)

        connection.commit()
        print("Segment Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

class Segment:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        #self.current_segment_key = property_ranges.get("segment_key", [])[1] - 1  # Initialize with the previous value
        #self.current_road_key = property_ranges.get("road_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "road_key":
                self.current_road_key += 1
                generated_data[property_name] = self.current_road_key
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
            seeder = Segment(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def insert_data_to_database(self, road_key):
        data = self.generate_random_data()
        insert_data_to_database([data], road_key)

property_ranges = {
    #"segment_key": ["int", 1, sys.maxsize],
    #"road_key": ["int", 1, sys.maxsize],
    "segment_name": ["choice", "...", "..."],
    "segment_type": ["choice", "...", "..."],
    "segment_length": ["int", 0, 1],
    "number_of_lanes": ["int", 1, 100],
    "start_point": ["float", 1, sys.maxsize],
    "end_point": ["float", 1, sys.maxsize],
}

def get_last_entry(key, table_name):
    conn = psycopg2.connect(
        host=constants.host,
        database=constants.db_name,
        user=constants.username,
        password=constants.password
    )
    cursor = conn.cursor()

    # Assuming your table name is "your_table_name" and the primary key column is "id"
    query = "SELECT " + key + " FROM " + table_name + " ORDER BY " + key + " DESC LIMIT 1;"

    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]  # Assuming primary key is a single value
    else:
        return None

def main():
    # Create a Seeder instance
    seeder = Segment(property_ranges)

    road_key = get_last_entry("road_key", "t_road")

    # Generate and print example data
    for _ in range(1):
        data = seeder.insert_data_to_database(road_key)

        return data

main()