class RoadEvent:
    def __init__(self, RoadEventKey, Description, Severity, Status, ImpactLevel):
        self.RoadEventKey = RoadEventKey
        self.Description = Description
        self.Severity = Severity
        self.Status = Status
        self.ImpactLevel = ImpactLevel

    def __str__(self):
        return self.RoadEventKey