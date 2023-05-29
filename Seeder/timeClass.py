import random
import sys


class Time:
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
            seeder = Time(self.property_ranges)
            seeders.append(seeder)
        return seeders


property_ranges = {
    "time_key": ["int", 1, sys.maxsize],
    "event_key": ["int", 1, sys.maxsize],
    "day": ["int", 1, 31],
    "month": ["int", 1, 12],
    "year": ["int", 2023, sys.maxsize],
    "is_weekend_day": ["choice", "True", "False"],
    "is_holiday": ["choice", "True", "False"],
    "trimester": ["int", 1, 3],
    "semester": ["int", 1, 2],
    "week_day_number": ["int", 1, 7],
    "week_day_name" : ["choice","Sunday","Monday","Tuesday","Wenesday","Thursday","Friday","Saturday"],
    "season" : ["choice", "Winter","Spring","Summer","Autumn"],
    "full_date_description" : ["choice", "13 January 2023"],
}

seeder_generator = Time(property_ranges)
n = 3  # Number of Seeder instances to generate
seeders = seeder_generator.generate_seeders(n)

for seeder in seeders:
    generated_messages = seeder.generate_random_data()
    print(generated_messages)
    print("---")