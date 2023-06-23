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
        cursor.execute("SELECT MAX(zone_key) FROM t_zone")
        max_zone_key = cursor.fetchone()[0]
        if max_zone_key is None:
            max_zone_key = 0

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_zone (zone_key, zone_name, zone_type, zone_description, zone_area) 
            VALUES (%s, %s, %s, %s, %s)
        """

        for record in data:
            max_zone_key += 1
            record['zone_key'] = max_zone_key

            values = (
                record['zone_key'],
                record['zone_name'],
                record['zone_type'],
                record['zone_description'],
                record['zone_area']
            )
            cursor.execute(insert_query, values)

        connection.commit()
        print("Zone Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()



class Zone:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_zone_key = property_ranges.get("zone_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "zone_key":
                self.current_zone_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_zone_key
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
                seeder = Zone(self.property_ranges)
                seeders.append(seeder)
            return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])


property_ranges = {
    "zone_key": ["int", 1, sys.maxsize],
    "zone_name": ["choice",
        "Lisbon",
        "Porto",
        "Vila Nova de Gaia",
        "Amadora",
        "Braga",
        "Funchal",
        "Coimbra",
        "Almada",
        "Setúbal",
        "Agualva-Cacém",
        "Queluz",
        "Aveiro",
        "Viseu",
        "Guimarães",
        "Oeiras",
        "Matosinhos",
        "Gondomar",
        "Sintra",
        "Faro",
        "Vila Franca de Xira",
        "Maia",
        "Évora",
        "Rio Tinto",
        "Câmara de Lobos",
        "Santarém",
        "Castelo Branco",
        "Barreiro",
        "Loures",
        "Póvoa de Varzim",
        "Sesimbra",
        "Vila Nova de Famalicão",
        "Ermesinde",
        "Portimão",
        "Ponta Delgada",
        "Quarteira",
        "Leiria",
        "Portalegre",
        "Beja",
        "Viana do Castelo",
        "Figueira da Foz",
        "Chaves",
        "Lamego",
        "Torres Vedras",
        "Caldas da Rainha",
        "Alcobaça",
        "Fátima",
        "Vila Nova de Milfontes",
        "Odemira",
        "Albufeira",
        "Lagos",
        "Tavira",
        "Loulé"
    ],
    "zone_type": ["choice", "unavailable", "increasedVolumeOfTraffic", "trafficJamSlowlyIncreasing"],
    "zone_description": ["choice", "open", "closed","restricted access","maintenance in progress","emergency situation"],
    "zone_area": ["choice", "Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo", "Vila Real y Viseu"],
}

# Create a Seeder instance
seeder = Zone(property_ranges)

# Generate and print example data
for _ in range(3):
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






