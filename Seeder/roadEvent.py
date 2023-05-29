import random
import sys


class RoadEvent:
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
            seeder = RoadEvent(self.property_ranges)
            seeders.append(seeder)
        return seeders


property_ranges = {
    "road_event_key": ["int", 1, sys.maxsize],
    "description": ["choice", "open", "closed"],
    "severity": ["int", 1, 10],
    "status": ["choice","in progress", "resolved"],
    "impact_level": ["choice","very-low","low","medium","high","very-high"],
}

seeder_generator = RoadEvent(property_ranges)
n = 3  # Number of Seeder instances to generate
seeders = seeder_generator.generate_seeders(n)

for seeder in seeders:
    generated_messages = seeder.generate_random_data()
    print(generated_messages)
    print("---")
