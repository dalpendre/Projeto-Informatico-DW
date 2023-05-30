import random
import sys


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


property_ranges = {
    "road_event_key": ["int", 1, sys.maxsize],
    "description": ["choice", "open", "closed"],
    "severity": ["int", 1, 10],
    "status": ["choice","in progress", "resolved"],
    "impact_level": ["choice","very-low","low","medium","high","very-high"],
}

# Create a Seeder instance
seeder = RoadEvent(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_random_data()
    print(data)
    print("---")
