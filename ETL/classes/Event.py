class Event:
    def __init__(self, EventKey, Designation, StartTime, EndTime, FlagSingleDayEvent):
        self.EventKey = EventKey
        self.Designation = Designation
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.FlagSingleDayEvent = FlagSingleDayEvent

    def __str__(self):
        return "EventKey: " + str(self.EventKey) + " Designation: " + str(self.Designation) + " StartTime: " + str(self.StartTime) + " EndTime: " + str(self.EndTime) + " FlagSingleDayEvent: " + str(self.FlagSingleDayEvent)