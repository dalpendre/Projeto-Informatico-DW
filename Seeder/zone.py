import random
import sys
import csv
import psycopg2
from psycopg2 import Error


def insert_data_to_database(data):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="12345678",
            host="18.169.68.102",
            port="5432",
            database="projeto_informatico_source_db"
        )

        cursor = connection.cursor()

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_zone (zone_key, zone_name, zone_type, zone_description, zone_area) 
            VALUES (%s, %s, %s, %s, %s)
        """

        for record in data:
            values = (
                record['zone_key'],
                record['zone_name'],
                record['zone_type'],
                record['zone_description'],
                record['zone_area']
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



class Zone:
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
                seeder = Zone(self.property_ranges)
                seeders.append(seeder)
            return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])


property_ranges = {
    "zone_key": ["int", 61, 70],
    "zone_name": ["choice", "unavailable", "increasedVolumeOfTraffic", "trafficJamSlowlyIncreasing"],
    "zone_type": ["choice", "unavailable", "increasedVolumeOfTraffic", "trafficJamSlowlyIncreasing"],
    "zone_description": ["choice", "open", "closed"],
    "zone_area": ["choice", "unavailable", "increasedVolumeOfTraffic", "trafficJamSlowlyIncreasing"],
}

seeder_generator = Zone(property_ranges)
n = 3  # Number of Seeder instances to generate
seeders = seeder_generator.generate_seeders(n)

for seeder in seeders:
    seeder.insert_data_to_database()

"""
    generated_messages = seeder.generate_random_data()
    print(generated_messages)
    print("---")
--------------------------------------------------------------
    def save_data_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the headers
            writer.writerow(self.property_ranges.keys())

            # Write the data
            for _ in range(n):
                data_generated = self.generate_random_data()
                writer.writerow(data_generated.values())

        print("CSV file saved successfully!")
        
file_path = 'test.csv'  # Replace with your desired file path
seeders[0].save_data_to_csv(file_path)
"""






