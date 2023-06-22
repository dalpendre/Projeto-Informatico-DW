import random
import sys
import datetime
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

        cursor.execute("SELECT MAX(time_key), MAX(event_key) FROM t_time")
        max_values = cursor.fetchone()
        max_time_key = max_values[0]
        max_event_key = max_values[1]

        if max_time_key is None:
            max_time_key = 0
        if max_event_key is None:
            max_event_key = 0

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_time (time_key,event_key,c_day,c_month,c_year,weekend_day,week_day_number,week_day_name,is_holiday,trimester,semester,season,full_date_description) 
            VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s,%s)
        """

        for record in data:
            max_time_key += 1
            max_event_key += 1
            record['time_key'] = max_time_key
            record['event_key'] = max_event_key

            values = (
                record['time_key'],
                record['event_key'],
                record['day'],
                record['month'],
                record['year'],
                record['is_weekend_day'],
                record['week_day_number'],
                record['week_day_name'],
                record['is_holiday'],
                record['trimester'],
                record['semester'],
                record['season'],
                record['full_date_description']
            )

            cursor.execute(insert_query, values)

        connection.commit()
        print("Time Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()


class Time:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_time_key = property_ranges.get("time_key", [])[1] - 1  # Initialize with the previous value
        self.current_event_key = property_ranges.get("event_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "time_key":
                self.current_time_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_time_key
            elif property_name == "event_key":
                self.current_event_key += 1
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
                seeder = Time(self.property_ranges)
                seeders.append(seeder)
            return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])


property_ranges = {
    "time_key": ["int", 1, sys.maxsize],
    "event_key": ["int", 1, sys.maxsize],
    "day": ["int", datetime.date.today().day, datetime.date.today().day],
    "month": ["int", datetime.date.today().month, datetime.date.today().month],
    "year": ["int", datetime.date.today().year, datetime.date.today().year],
    "is_weekend_day": ["boolean"],
    "is_holiday": ["boolean"],
    "trimester": ["int", 1, 3],
    "semester": ["int", 1, 2],
    "week_day_number": ["int", 1, 7],
    "week_day_name" : ["choice","Sunday","Monday","Tuesday","Wenesday","Thursday","Friday","Saturday"],
    "season" : ["choice", "Winter","Spring","Summer","Autumn"],
    "full_date_description" : ["choice", datetime.date.today().strftime("%d %B %Y")],
}

# Create a Seeder instance
seeder = Time(property_ranges)

# Generate and print example data
for _ in range(3):
    seeder.insert_data_to_database()

"""
data = seeder.generate_random_data()
print(data)
print("---")
"""
