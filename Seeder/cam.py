import random
import sys
from datetime import datetime

import psycopg2
from psycopg2 import Error
import pandas as pd
import requests

import constants
import road
import event
import segment
import timeClass #time class to store date info, not the time python package

def get_elevation(latitude, longitude):
    url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={latitude},{longitude}&key=" + constants.google_maps_api_key
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        elevation = data['results'][0]['elevation']
        return elevation
    else:
        return 0

def datetime_to_timestamp(datetime_str):
    datetime_obj = datetime.fromisoformat(datetime_str)
    timestamp = datetime_obj.timestamp()
    normalized_timestamp = int(timestamp * 1000)  # Convert to milliseconds

    min_timestamp = 0
    max_timestamp = 4398046511103

    normalized_timestamp = max(min_timestamp, min(max_timestamp, normalized_timestamp))  # Clamp within the range

    return normalized_timestamp

#extract timestamp and coordinates from csv file
def file_extract(path):

    data = pd.read_csv(path)

    selected_columns = ['/createdAt', '/capturedData/locationLatitude', '/capturedData/locationLongitude']  # Replace with the actual column names
    selected_data = data[selected_columns]

    return selected_data

def insert_data_to_database(data, timestamp, latitude, longitude, altitude, time_key, segment_key, num_lines):

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
                time_key,
                segment_key,
                record['station_id'],
                latitude,
                longitude,
                altitude,
                record['speed'],
                record['heading'],
                record['acceleration'],
                record['station_type'],
                record['vehicle_role'],
                timestamp,
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
        #self.current_time_key = property_ranges.get("time_key", [])[1] - 1  # Initialize with the previous value
        #self.current_segment_key = property_ranges.get("segment_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            #if property_name == "time_key":
                #self.current_time_key += 1
                #generated_data[property_name] = self.current_time_key
            #elif property_name == "segment_key":
                #self.current_segment_key += 1
                #generated_data[property_name] = self.current_segment_key
            #else:
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

    def generate_insert_data_to_database(self, timestamp, latitude, longitude, altitude, time_key, segment_key, num_lines):
        data = self.generate_random_data()
        insert_data_to_database([data], timestamp, latitude, longitude, altitude, time_key, segment_key, num_lines)

property_ranges = {
    #"time_key" : ["int", 1, sys.maxsize],
    #"segment_key" : ["int", 1, sys.maxsize],
    "station_id" : ["int", 0, 4294967295],
    #"latitude" : ["int", -900000000, 900000000],
    #"longitude" : ["int", -1800000000, 1800000000],
    #"altitude" : ["int", -100000, 800001],
    "speed" : ["float", 0, 16383],
    "heading" : ["int", 0, 3601],
    "acceleration" : ["int", -160, 160],
    "station_type": ["int", 0, 255],
    "vehicle_role": ["int",0,15],
    #"time_stamp" : ["int", 1, 4398046511103],
    "fuel_type": ["choice", "000", "001", "010", "011", "100", "101", "110"],
    "activation_data": ["choice", "000", "001", "010", "011", "100", "101", "110"],
    "stationary_since": ["int", 0, 3]
}

# Create a Seeder instance
seeder = Cam(property_ranges)

latitude_longitude_convert_factor = 0.0000001

# extract data from dataset her
dataset_data = file_extract("casa estg-11-04-2023-08-58-00.csv")

event = event.main_empty()
road = road.main()
time = timeClass.main()
#print("New road: ", road)
#print("New time: ", time)
#print("New empty event: ", event)

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

road_key = get_last_entry("road_key", "t_road")
print("RoadKey: ", road_key)
time_key = get_last_entry("time_key", "t_time")
print("TimeKey: ", time_key)

dataset_num_lines = len(dataset_data)

num_segments = dataset_num_lines / 2
print("Número de segmentos: ", num_segments)

prev_latitude = None
prev_longitude = None
# Generate and print example data
for index, row in dataset_data.iterrows():

    timestamp = datetime_to_timestamp(row['/createdAt'])
    latitude = float(row['/capturedData/locationLatitude']) * latitude_longitude_convert_factor
    longitude = float(row['/capturedData/locationLongitude']) * latitude_longitude_convert_factor
    altitude = get_elevation(latitude, longitude)

    # generate segments (every set of different coordinates is a segment)
    if latitude != prev_latitude or longitude != prev_longitude:
        # Latitude or longitude has changed
        print("Change detected at index:", index)
        # Do something with the changed values

        #create new segment
        segment.main()

        segment_key = get_last_entry("segment_key", "t_segment")
        print("Segment key: ", segment_key)

    prev_latitude = latitude
    prev_longitude = longitude

    seeder.generate_insert_data_to_database(timestamp, latitude, longitude, altitude, time_key, segment_key, dataset_num_lines)
    print(index, timestamp, latitude, longitude, altitude)