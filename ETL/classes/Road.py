class Road:
    def __init__(self, RoadKey, RoadName, RoadType, RoadLength, NumberOfLanes, StartPoint, EndPoint):
        self.RoadKey = RoadKey
        self.RoadName = RoadName
        self.RoadType = RoadType
        self.RoadLength = RoadLength
        self.NumberOfLanes = NumberOfLanes
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint

    def __str__(self):
        return "RoadKey: " + str(self.RoadKey) + "\nRoadName: " + str(self.RoadName) + "\nRoadType: " + str(self.RoadType) + "\nRoadLength: " + str(self.RoadLength) + "\nNumberOfLanes: " + str(self.NumberOfLanes) + "\nStartPoint: " + str(self.StartPoint) + "\nEndPoint: " + str(self.EndPoint)