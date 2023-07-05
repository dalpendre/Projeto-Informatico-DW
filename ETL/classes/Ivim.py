class IvimMessage:
    def __init__(self, ivim_key,road_sign_key, zone_key, latitude, longitude, altitude):
        self.ivim_key = ivim_key
        self.road_sign_key = road_sign_key
        self.zone_key = zone_key
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def __str__(self):
        pass