import random
import sys
import datetime

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
        else:
            return None


property_ranges = {
    "time_key": ["int", 1, sys.maxsize],
    "event_key": ["int", 1, sys.maxsize],
    "day": ["int", 1, 31],
    "month": ["int", 1, 12],
    "year": ["int", datetime.date.today().year, datetime.date.today().year],
    "is_weekend_day": ["choice", "True", "False"],
    "is_holiday": ["choice", "True", "False"],
    "trimester": ["int", 1, 3],
    "semester": ["int", 1, 2],
    "week_day_number": ["int", 1, 7],
    "week_day_name" : ["choice","Sunday","Monday","Tuesday","Wenesday","Thursday","Friday","Saturday"],
    "season" : ["choice", "Winter","Spring","Summer","Autumn"],
    "full_date_description" : ["choice", "13 January 2023"],
}

# Create a Seeder instance
seeder = Time(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_random_data()
    print(data)
    print("---")