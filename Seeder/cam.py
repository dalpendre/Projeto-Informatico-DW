import random
import sys
import psycopg2
from psycopg2 import Error
import pandas as pd
import constants

#extract timestamp and coordinates from csv file
def file_extract(path):
    data = pd.read_csv(path)

    #selected_columns = ['/createdAt', '/capturedData/locationLatitude', '/capturedData/locationLongitude']  # Replace with the actual column names
    #selected_data = data[selected_columns]

    return data

def insert_data_to_database(data):

    print(file_extract("casa estg-11-04-2023-08-58-00.csv"))

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
            INSERT INTO t_cam (time_key,segment_key,station_id,latitude,longitude,altitude,speed,
            heading,acceleration,station_type,vehicle_role,time_stamp,fuel_type,activation_data,stationary_since)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for record in data:
            values = (
                record['time_key'],
                record['segment_key'],
                record['station_id'],
                record['latitude'],
                record['longitude'],
                record['altitude'],
                record['speed'],
                record['heading'],
                record['acceleration'],
                record['station_type'],
                record['vehicle_role'],
                record['time_stamp'],
                record['fuel_type'],
                record['activation_data'],
                record['stationary_since']
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

class Cam:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_time_key = property_ranges.get("time_key", [])[1] - 1  # Initialize with the previous value
        self.current_segment_key = property_ranges.get("segment_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "time_key":
                self.current_time_key += 1
                generated_data[property_name] = self.current_time_key
            elif property_name == "segment_key":
                self.current_segment_key += 1
                generated_data[property_name] = self.current_segment_key
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
            seeder = Cam(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def generate_insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])

property_ranges = {
    "time_key" : ["int", 1, sys.maxsize],
    "segment_key" : ["int", 1, sys.maxsize],
    "station_id" : ["int", 0, 4294967295],
    "latitude" : ["int", -900000000, 900000000],
    "longitude" : ["int", -1800000000, 1800000000],
    "altitude" : ["int", -100000, 100000],
    "speed" : ["float", 0, 16383],
    "heading" : ["int", 0, 3601],
    "acceleration" : ["int", -160, 160],
    "station_type": ["int", 0, 255],
    "vehicle_role": ["int",0,15],
    "time_stamp" : ["int", 1, 4398046511103],
    "fuel_type": ["choice", "000", "001", "010", "011", "100", "101", "110"],
    "activation_data": ["choice", "000", "001", "010", "011", "100", "101", "110"],
    "stationary_since": ["int", 0, 3]
}

# Create a Seeder instance
seeder = Cam(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_insert_data_to_database()
    print(data)
    print("---")