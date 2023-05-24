class Road:
    def __init__(self, road_key, road_name, road_type, road_length, number_of_lanes, start_point, end_point):
        self.road_key = road_key
        self.road_name = road_name
        self.road_type = road_type
        self.road_length = road_length
        self.number_of_lanes = number_of_lanes
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return "Road: " + self.road_key + " " + self.road_name + " " + self.road_type + " " + self.road_length + " " + self.number_of_lanes + " " + self.start_point + " " + self.end_point