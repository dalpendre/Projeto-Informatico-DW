class Zone:
    def __init__(self, ZoneKey, ZoneName, ZoneType, ZoneDescription, ZoneArea):
        self.ZoneKey = ZoneKey
        self.ZoneName = ZoneName
        self.ZoneType = ZoneType
        self.ZoneDescription = ZoneDescription
        self.ZoneArea = ZoneArea

    def __str__(self):
        return "ZoneKey: " + str(self.ZoneKey) + "\nZoneName: " + str(self.ZoneName) + "\nZoneType: " + str(self.ZoneType) + "\nZoneDescription: " + str(self.ZoneDescription) + "\nZoneArea: " + str(self.ZoneArea)