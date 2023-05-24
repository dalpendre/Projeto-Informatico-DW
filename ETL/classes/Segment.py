class Segment:
    def __init__(self, segment_key, road_key, segment_name, segment_type, segment_length, number_of_lanes, start_point, end_point):
        self.segment_key = segment_key
        self.road_key = road_key
        self.segment_name = segment_name
        self.segment_type = segment_type
        self.segment_length = segment_length
        self.number_of_lanes = number_of_lanes
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return "SegmentKey: " + str(self.segment_key)