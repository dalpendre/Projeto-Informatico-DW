class IvimMessage:
    def __init__(self, IVIMKey, RoadSignKey, ZoneKey, Latitude, Longitude, Altitude):
        self.IVIMKey = IVIMKey
        self.RoadSignKey = RoadSignKey
        self.ZoneKey = ZoneKey
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Altitude = Altitude

    def __str__(self):
        return "IVIMKey: " + str(self.IVIMKey) + "\nRoadSignKey: " + str(self.RoadSignKey) + "\nZoneKey: " + str(self.ZoneKey) + "\nLatitude: " + str(self.Latitude) + "\nLongitude: " + str(self.Longitude) + "\nAltitude: " + str(self.Altitude)