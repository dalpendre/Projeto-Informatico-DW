class RoadSign:
    def __init__(self, road_sign_key, road_sign_description, road_sign_code, road_sign_symbol, road_sign_class, road_sign_visibility):
        self.road_sign_key = road_sign_key
        self.road_sign_description = road_sign_description
        self.road_sign_code = road_sign_code
        self.road_sign_symbol = road_sign_symbol
        self.road_sign_class = road_sign_class
        self.road_sign_visibility = road_sign_visibility

    def __str__(self):
        return "RoadSign: " + self.road_sign_key + " " + self.road_sign_description + " " + self.road_sign_code + " " + self.road_sign_symbol + " " + self.road_sign_class + " " + self.road_sign_visibility