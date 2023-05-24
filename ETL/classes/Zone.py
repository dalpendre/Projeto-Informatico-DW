class Zone:
    def __init__(self, zone_key, zone_name, zone_type, zone_description, zone_area):
        self.zone_key = zone_key
        self.zone_name = zone_name
        self.zone_type = zone_type
        self.zone_description = zone_description
        self.zone_area = zone_area

    def __str__(self):
        return "ZoneKey: " + str(self.zone_key) + "\nZoneName: " + str(self.zone_name) + "\nZoneType: " + str(self.zone_type) + "\nZoneDescription: " + str(self.zone_description) + "\nZoneArea: " + str(self.zone_area)