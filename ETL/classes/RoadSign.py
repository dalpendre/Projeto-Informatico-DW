class RoadSign:
    def __init__(self, RoadSignKey, RoadSignDescription, RoadType, RoadCode, RoadSymbol, RoadClass, RoadVisibility):
        self.RoadSignKey = RoadSignKey
        self.RoadSignDescription = RoadSignDescription
        self.RoadType = RoadType
        self.RoadCode = RoadCode
        self.RoadSymbol = RoadSymbol
        self.RoadClass = RoadClass
        self.RoadVisibility = RoadVisibility

    def __str__(self):
        return "RoadSignKey: " + str(self.RoadSignKey) + "\nRoadSignDescription: " + str(self.RoadSignDescription) + "\nRoadType: " + str(self.RoadType) + "\nRoadCode: " + str(self.RoadCode) + "\nRoadSymbol: " + str(self.RoadSymbol) + "\nRoadClass: " + str(self.RoadClass) + "\nRoadVisibility" + str(self.RoadVisibility)