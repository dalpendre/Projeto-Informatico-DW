class CamMessage:
    def __init__(self, CAMKey, StationID, Speed, Heading, Acceleration, StationType, VehicleRole, TypeOfFuel,
                 TimeStamp, BrakePedalEngaged, GasPedalEngaged, EmergencyPedalEngaged, CollisionWarningEngaged,
                 SpeedLimiterEngaged, CruiseControlEngaged, StationarySince, Latitude, Longitude, Altitude):
        self.CAMKey = CAMKey
        self.StationID = StationID
        self.Speed = Speed
        self.Heading = Heading
        self.Acceleration = Acceleration
        self.StationType = StationType
        self.VehicleRole = VehicleRole
        self.TypeOfFuel = TypeOfFuel
        self.TimeStamp = TimeStamp
        self.BrakePedalEngaged = BrakePedalEngaged
        self.GasPedalEngaged = GasPedalEngaged
        self.EmergencyPedalEngaged = EmergencyPedalEngaged
        self.CollisionWarningEngaged = CollisionWarningEngaged
        self.SpeedLimiterEngaged = SpeedLimiterEngaged
        self.CruiseControlEngaged = CruiseControlEngaged
        self.StationarySince = StationarySince
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Altitude = Altitude

    def __str__(self):
        return "CAMKey: " + str(self.CAMKey) + "\nStationID: " + str(self.StationID) + "\nSpeed: " + str(self.Speed) + "\nHeading: " + str(self.Heading) + "\nAcceleration: " + str(self.Acceleration) + "\nStationType: " + str(self.StationType) + "\nVehicleRole: " + str(self.VehicleRole) + "\nTypeOfFuel: " + str(self.TypeOfFuel) + "\nTimeStamp: " + str(self.TimeStamp) + "\nBrakePedalEngaged: " + str(self.BrakePedalEngaged) + "\nGasPedalEngaged: " + str(self.GasPedalEngaged) + "\nEmergencyPedalEngaged: " + str(self.EmergencyPedalEngaged) + "\nCollisionWarningEngaged: " + str(self.CollisionWarningEngaged) + "\nSpeedLimiterEngaged: " + str(self.SpeedLimiterEngaged) + "\nCruiseControlEngaged: " + str(self.CruiseControlEngaged) + "\nStationarySince: " + str(self.StationarySince) + "\nLatitude: " + str(self.Latitude) + "\nLongitude: " + str(self.Longitude) + "\nAltitude: " + str(self.Altitude)