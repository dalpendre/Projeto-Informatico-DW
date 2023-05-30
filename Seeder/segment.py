import random
import sys


class Segment:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_segment_key = property_ranges.get("segment_key", [])[1] - 1  # Initialize with the previous value
        self.current_road_key = property_ranges.get("road_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "segment_key":
                self.current_segment_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_segment_key
            elif property_name == "road_key":
                self.current_road_key += 1
                generated_data[property_name] = self.current_road_key
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
            seeder = Segment(self.property_ranges)
            seeders.append(seeder)
        return seeders


property_ranges = {
    "segment_key": ["int", 1, sys.maxsize],
    "road_key": ["int", 1, sys.maxsize],
    "segment_name": ["choice", "...", "..."],
    "segment_type": ["choice", "...", "..."],
    "segment_length": ["int", 0, sys.maxsize],
    "number_of_lanes": ["int", 1, sys.maxsize],
    "start_point": ["float", 1, sys.maxsize],
    "end_point": ["float", 1, sys.maxsize],
}

# Create a Seeder instance
seeder = Segment(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_random_data()
    print(data)
    print("---")