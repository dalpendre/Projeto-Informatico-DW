import random
import sys

class Ivim:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_ivim_key = property_ranges.get("ivim_key", [])[1] - 1  # Initialize with the previous value
        self.current_zone_key = property_ranges.get("zone_key", [])[1] - 1  # Initialize with the previous value
        self.current_road_sign_key = property_ranges.get("road_sign_key", [])[1] - 1  # Initialize with the previous value
    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "ivim_key":
                self.current_ivim_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_ivim_key
            elif property_name == "zone_key":
                self.current_zone_key += 1
                generated_data[property_name] = self.current_zone_key
            elif property_name == "road_sign_key":
                self.current_road_sign_key += 1
                generated_data[property_name] = self.current_road_sign_key
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

    """def generate_seeders(self, n):
        seeders = []
        for _ in range(n):
            seeder = Ivim(self.property_ranges)
            seeders.append(seeder)
        return seeders
    """

property_ranges = {
    "ivim_key" : ["int", 1, sys.maxsize],
    "zone_key" : ["int", 1, sys.maxsize],
    "road_sign_key" : ["int", 1, sys.maxsize],
    "latitude" : ["int", -900000000, 900000000],
    "longitude" : ["int", -1800000000, 1800000000],
    "altitude" : ["int", -100000, 100000],
}
"""
seeder_generator = Ivim(property_ranges)
n = 2  # Number of Seeder instances to generate
seeders = seeder_generator.generate_seeders(n)

for seeder in seeders:
    generated_messages = seeder.generate_random_data()
    print(generated_messages)
    print("---")
"""
# Create a Seeder instance
seeder = Ivim(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_random_data()
    print(data)
    print("---")

