class Segment:
    def __init__(self, SegmentKey, RoadKey, StartPoint, EndPoint, SegmentLength, SegmentName, SegmentType, NumberOfLanes):
        self.SegmentKey = SegmentKey
        self.RoadKey = RoadKey
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.SegmentLength = SegmentLength
        self.SegmentName = SegmentName
        self.SegmentType = SegmentType
        self.NumberOfLanes = NumberOfLanes

    def __str__(self):
        return "SegmentKey: " + str(self.SegmentKey)