class Event:
    def __init__(self, event_key, designation, start_time, end_time, flag_single_day_event):
        self.event_key = event_key
        self.designation = designation
        self.start_time = start_time
        self.end_time = end_time
        self.flag_single_day_event = flag_single_day_event

    def __str__(self):
        return "EventKey: " + str(self.event_key) + "\nDesignation: " + str(self.designation) + "\nStartTime: " + str(self.start_time) + "\nEndTime: " + str(self.end_time) + "\nFlagSingleDayEvent: " + str(self.flag_single_day_event)