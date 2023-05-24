class RoadEvent:
    def __init__(self, road_event_key, description, severity, status, impact_level):
        self.road_event_key = road_event_key
        self.description = description
        self.severity = severity
        self.status = status
        self.impact_level = impact_level

    def __str__(self):
        return self.road_event_key + " " + self.description + " " + self.severity + " " + self.status + " " + self.impact_level