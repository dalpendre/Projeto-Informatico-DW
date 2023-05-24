class IvimMessage:
    def __init__(self, ivim_key, road_sign_key, zone_key, latitude, longitude, altitude):
        self.ivim_key = ivim_key
        self.road_sign_key = road_sign_key
        self.zone_key = zone_key
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def __str__(self):
        return "IvimKey: " + str(self.ivim_key) + "\nRoadSignKey: " + str(self.road_sign_key) + "\nZoneKey: " + str(self.zone_key) + "\nLatitude: " + str(self.latitude) + "\nLongitude: " + str(self.longitude) + "\nAltitude: " + str(self.altitude)