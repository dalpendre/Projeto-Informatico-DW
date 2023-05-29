import random
import sys

class Cam:
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
                seeder = Cam(self.property_ranges)
                seeders.append(seeder)
            return seeders

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
    "stationary_since" : ["float", 1.0, 10.0],
}

seeder_generator = Cam(property_ranges)
n = 3  # Number of Seeder instances to generate
seeders = seeder_generator.generate_seeders(n)

for seeder in seeders:
    generated_messages = seeder.generate_random_data()
    print(generated_messages)
    print("---")

