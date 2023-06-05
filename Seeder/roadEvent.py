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
            INSERT INTO t_road_event (road_event_key,description,severity,status,impact_level) 
            VALUES (%s, %s, %s, %s, %s)
        """

        for record in data:
            values = (
                record['road_event_key'],
                record['description'],
                record['severity'],
                record['status'],
                record['impact_level']
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


class RoadEvent:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_road_event_key = property_ranges.get("road_event_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "road_event_key":
                self.current_road_event_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_road_event_key
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
            seeder = RoadEvent(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])


property_ranges = {
    "road_event_key": ["int", 1, sys.maxsize],
    "description": ["choice", "Traffic Accident", "Road Construction","Road Closure","Road Congestion","Road Flooding","Roadwork Zone","Vehicle Breakdown","Traffic Jam","Road Debris","Traffic Control"],
    "severity": ["int", 1, 10],
    "status": ["choice","in progress", "resolved"],
    "impact_level": ["choice","very-low","low","medium","high","very-high"],
}

# Create a Seeder instance
seeder = RoadEvent(property_ranges)

# Generate and print example data
for _ in range(3):
    seeder.insert_data_to_database()


    
"""
data = seeder.generate_random_data()
print(data)
print("---")
"""
