import random
import sys

from data import RoadSignData

class RoadSign:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.curret_road_sign_key = property_ranges.get("road_sign_key", [])[1] - 1  # Initialize with the previous value


    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "road_sign_key":
                self.curret_road_sign_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.curret_road_sign_key
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

property_ranges = {
    "road_sign_key" : ["int", 1, sys.maxsize],
    "road_sign_description": ["choice", "...", "..."],
    "code" : ["int", 1, sys.maxsize],
    "symbol": ["choice", "open", "closed"],
    "class_code" : ["int", 0, 100],
    "visibility": ["choice", "important", "..."],
}

# Create a Seeder instance
seeder = RoadSign(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_random_data()
    print(data)
    print("---")