import random

class Seeder:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges

    def generate_messages(self, n):
        messages = []
        for _ in range(n):
            message = {}
            for prop, prop_range in self.property_ranges.items():
                value = random.randint(prop_range[0], prop_range[1])
                message[prop] = value
            messages.append(message)
        return messages

class SeederGenerator:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges

    def generate_seeders(self, n):
        seeders = []
        for _ in range(n):
            seeder = Seeder(self.property_ranges)
            seeders.append(seeder)
        return seeders

property_ranges = {
    'property1': (10, 50),
    'property2': (1, 100),
    'property3': (-5, 5)
}

seeder_generator = SeederGenerator(property_ranges)
n = 3  # Number of Seeder instances to generate
seeders = seeder_generator.generate_seeders(n)

for seeder in seeders:
    generated_messages = seeder.generate_messages(5)
    print(generated_messages)
    print("---")
