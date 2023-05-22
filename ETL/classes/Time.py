class Time:
    def __init__(self, TimeKey, EventKey, CDay, CMonth, CYear, CWeekendDay, CWeekDayNumber, CWeekDayName, CIsHoliday, CTrimester, CSemester, CSeason, CFullDateDescription):
        self.TimeKey = TimeKey
        self.EventKey = EventKey
        self.CDay = CDay
        self.CMonth = CMonth
        self.CYear = CYear
        self.CWeekendDay = CWeekendDay
        self.CWeekDayNumber = CWeekDayNumber
        self.CWeekDayName = CWeekDayName
        self.CIsHoliday = CIsHoliday
        self.CTrimester = CTrimester
        self.CSemester = CSemester
        self.CSeason = CSeason
        self.CFullDateDescription = CFullDateDescription

    def __str__(self):
        return "TimeKey: " + str(self.TimeKey) + "\nEventKey: " + str(self.EventKey) + "\nDay: " + str(self.CDay) + "\nMonth: " + str(self.CMonth) + "\nYear: " + str(self.CYear) + "\nWeekendDay: " + str(self.CWeekendDay) + "\nWeekDayNumber: " + str(self.CWeekDayNumber) + "\nWeekDayName: " + str(self.CWeekDayName) + "\nIsHoliday: " + str(self.CIsHoliday) + "\nTrimester: " + str(self.CTrimester) + "\nSemester: " + str(self.CSemester) + "\nSeason: " + str(self.CSeason) + "\nFullDateDescription: " + str(self.CFullDateDescription)