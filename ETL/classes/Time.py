class Time:
    def __init__(self, event_key, c_day, c_month, c_year, weekend_day, week_day_number, week_day_name, is_holiday,
    trimester, semester, season, full_date_description):
        self.event_key = event_key
        self.c_day = c_day
        self.c_month = c_month
        self.c_year = c_year
        self.weekend_day = weekend_day
        self.week_day_number = week_day_number
        self.week_day_name = week_day_name
        self.is_holiday = is_holiday
        self.trimester = trimester
        self.semester = semester
        self.season = season
        self.full_date_description = full_date_description

    def __str__(self):
        pass