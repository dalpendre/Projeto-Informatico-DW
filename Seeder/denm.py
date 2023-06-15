import random
import sys
import psycopg2
from psycopg2 import Error

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

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_time (denm_key,time_key,road_event_key,time_stamp,latitude,longitude,altitude,heading,cause,traffic_cause,road_works_sub_cause,accident_sub_cause,slow_vehicle_sub_cause,stationary_vehicle_cause,human_problem_sub_cause,collision_risk_sub_cause,dangerous_situation_sub_cause,vehicle_break_down_sub_cause,post_crash_sub_cause,human_presence_on_the_road_sub_cause,adverse_weather_condition_extreme_weather_condition_sub_cause,adverse_weather_condition_adhesion_sub_cause,adverse_weather_condition_visibility_sub_cause,adverse_weather_condition_precipitation_sub_cause,emergency_vehicle_approaching_sub_cause,hazardous_location_surface_condition_sub_cause,hazardous_location_obstacle_on_the_road_sub_cause,hazardous_location_animal_on_the_road_sub_cause,rescue_and_recovery_work_in_progress_sub_cause,dangerous_end_of_queue_sub_cause) 
            VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)
        """

        for record in data:
            values = (
                record['denm_key'],
                record['time_key'],
                record['road_event_key'],
                record['time_stamp'],
                record['latitude'],
                record['longitude'],
                record['altitude'],
                record['heading'],
                record['cause'],
                record['traffic_cause'],
                record['road_works_sub_cause'],
                record['accident_sub_cause'],
                record['slow_vehicle_sub_cause'],
                record['stationary_vehicle_cause'],
                record['human_problem_sub_cause'],
                record['collision_risk_sub_cause'],
                record['dangerous_situation_sub_cause'],
                record['vehicle_break_down_sub_cause'],
                record['post_crash_sub_cause'],
                record['human_presence_on_the_road_sub_cause'],
                record['adverse_weather_condition_extreme_weather_condition_sub_cause'],
                record['adverse_weather_condition_adhesion_sub_cause'],
                record['adverse_weather_condition_visibility_sub_cause'],
                record['adverse_weather_condition_precipitation_sub_cause'],
                record['emergency_vehicle_approaching_sub_cause'],
                record['hazardous_location_surface_condition_sub_cause'],
                record['hazardous_location_obstacle_on_the_road_sub_cause'],
                record['hazardous_location_animal_on_the_road_sub_cause'],
                record['rescue_and_recovery_work_in_progress_sub_cause'],
                record['dangerous_end_of_queue_sub_cause']

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


class Denm:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_denm_key = property_ranges.get("denm_key", [])[1] - 1  # Initialize with the previous value
        self.current_road_event_key = property_ranges.get("road_event_key", [])[1] - 1  # Initialize with the previous value
        self.current_time_key = property_ranges.get("time_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "denm_key":
                self.current_denm_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_denm_key
            elif property_name == "road_event_key":
                self.current_road_event_key += 1
                generated_data[property_name] = self.current_road_event_key
            elif property_name == "time_key":
                self.current_time_key += 1
                generated_data[property_name] = self.current_time_key
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
            seeder = Denm(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])

property_ranges = {
    "denm_key": ["int", 1, sys.maxsize],
    "road_event_key": ["int", 1, sys.maxsize],
    "time_key": ["int", 1, sys.maxsize],
    "heading": ["int", 0, 3601],
    "time_stamp": ["int", 0, 4398046511103],
    "longitude": ["int", -1800000000, 1800000000],
    "latitude": ["int", -900000000, 900000000],
    "altitude": ["int", -100000, 100000],
    "cause": ["int", 0, 99],
    "traffic_cause": ["int", 0, 8],
    "accident_sub_cause": ["int", 0, 8],
    "road_works_sub_cause" : ["int", 0, 6],
    "human_presence_on_the_road_sub_cause": ["int", 0, 3],
    "wrong_way_driving_sub_cause": ["int", 0, 2],
    "adverse_weather_condition_extreme_weather_condition_sub_cause": ["int", 0, 6],
    "adverse_weather_condition_adhesion_sub_cause": ["int", 0, 10],
    "adverse_weather_condition_visibility_sub_cause": ["int", 0, 8],
    "adverse_weather_condition_precipitation_sub_cause": ["int", 0, 3],
    "slow_vehicle_sub_cause": ["int", 0, 8],
    "stationary_vehicle_sub_cause": ["int", 0, 5],
    "human_problem_sub_cause": ["int", 0, 2],
    "emergency_vehicle_approaching_sub_cause": ["int", 0, 2],
    "hazardous_location_dangerous_curve_sub_cause": ["int", 0, 5],
    "hazardous_location_surface_condition_sub_cause": ["int", 0, 9],
    "hazardous_location_obstacle_on_the_road_sub_cause": ["int", 0, 7],
    "hazardous_location_animal_on_the_road_sub_cause": ["int", 0, 4],
    "collision_risk_sub_cause": ["int", 0, 4],
    "signal_violation_sub_cause": ["int", 0, 3],
    "rescue_and_recovery_work_in_progress_sub_cause": ["int", 0, 5],
    "dangerous_end_of_queue_sub_cause": ["int", 0, 4],
    "dangerous_situation_sub_cause": ["int", 0, 7],
    "vehicle_break_down_sub_cause": ["int", 0, 9],
    "post_crash_sub_cause": ["int", 0, 4],
}

# Create a Seeder instance
seeder = Denm(property_ranges)

# Generate and print example data
for _ in range(3):
    seeder.insert_data_to_database()


    
"""
data = seeder.generate_random_data()
print(data)
print("---")
"""