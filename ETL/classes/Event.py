class Event:
    def __init__(self, designation, start_time, end_time, flag_single_day_event):
        self.designation = designation
        self.start_time = start_time
        self.end_time = end_time
        self.flag_single_day_event = flag_single_day_event

    def __str__(self):
        pass