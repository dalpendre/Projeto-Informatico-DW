import random
import sys

class Cam:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_cam_key = property_ranges.get("cam_key", [])[1] - 1  # Initialize with the previous value
        self.current_time_key = property_ranges.get("time_key", [])[1] - 1  # Initialize with the previous value
        self.current_segment_key = property_ranges.get("segment_key", [])[1] - 1  # Initialize with the previous value


    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "cam_key":
                self.current_cam_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_cam_key
            elif property_name == "time_key":
                self.current_time_key += 1
                generated_data[property_name] = self.current_time_key
            elif property_name == "segment_key":
                self.current_segment_key += 1
                generated_data[property_name] = self.current_segment_key
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
    "cam_key" : ["int", 1, sys.maxsize],
    "time_key" : ["int", 1, sys.maxsize],
    "segment_key" : ["int", 1, sys.maxsize],
    "station_id" : ["int", 0, 4294967295],
    "latitude" : ["int", -900000000, 900000000],
    "longitude" : ["int", -1800000000, 1800000000],
    "altitude" : ["int", -100000, 100000],
    "speed" : ["float", 0, 16383],
    "heading" : ["int", 0, 3601],
    "acceleration" : ["int", -160, 160],
    "station_type": ["int", 0, 255],
    "vehicle_role": ["int",0,15],
    "time_stamp" : ["int", 1, 4398046511103],
    "type_of_fuel": ["choice","human_powered", "hydrogenStorage", "electricEnergyStorage", "liquidPropaneGas", "compressedNaturalGas", "diesel", "gasoline", "ammonia"],
    "brake_pedal_engaged" : ["choice", "True", "False"],
    "gas_pedal_engaged" : ["choice", "True", "False"],
    "emergency_pedal_engaged" : ["choice", "True", "False"],
    "collision_warning_engaged" : ["choice", "True", "False"],
    "acc_engaged" : ["choice", "True", "False"],
    "cruise_control_engaged" : ["choice", "True", "False"],
    "speed_limiter_engaged" : ["choice", "True", "False"],
    "stationary_since" : ["int", 0, 3],
}

# Create a Seeder instance
seeder = Cam(property_ranges)

# Generate and print example data
for _ in range(3):
    data = seeder.generate_random_data()
    print(data)
    print("---")

