class DenmMessage:
    def __init__(self, time_key, road_event_key, time_stamp, latitude, longitude, altitude, heading, cause, traffic_cause, road_works_sub_cause,
                 accident_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_sub_cause, human_presence_on_the_road_sub_cause,
                 collision_risk_sub_cause, dangerous_situation_sub_cause, vehicle_break_down_sub_cause, post_crash_sub_cause,
                 human_problem_sub_cause, adverse_weather_condition_extreme_weather_condition_sub_cause, adverse_weather_condition_adhesion_sub_cause,
                 adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause, emergency_vehicle_approaching_sub_cause,
                 hazardous_location_dangerous_curve_sub_cause, hazardous_location_surface_condition_sub_cause, hazardous_location_obstacle_on_the_road_sub_cause,
                 hazardous_location_animal_on_the_road_sub_cause, rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause,
                 signal_violation_sub_cause, wrong_way_driving_sub_cause):
        self.time_key = time_key
        self.road_event_key = road_event_key
        self.time_stamp = time_stamp
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.heading = heading
        self.cause = cause
        self.traffic_sub_cause = traffic_cause
        self.accident_sub_cause = accident_sub_cause
        self.road_works_sub_cause = road_works_sub_cause
        self.human_presence_on_the_road_sub_cause = human_presence_on_the_road_sub_cause
        self.wrong_way_driving_sub_cause = wrong_way_driving_sub_cause
        self.adverse_weather_condition_extreme_weather_condition_sub_cause = adverse_weather_condition_extreme_weather_condition_sub_cause
        self.adverse_weather_condition_adhesion_sub_cause = adverse_weather_condition_adhesion_sub_cause
        self.adverse_weather_condition_visibility_sub_cause = adverse_weather_condition_visibility_sub_cause
        self.adverse_weather_condition_precipitation_sub_cause = adverse_weather_condition_precipitation_sub_cause
        self.slow_vehicle_sub_cause = slow_vehicle_sub_cause
        self.stationary_vehicle_sub_cause = stationary_vehicle_sub_cause
        self.human_problem_sub_cause = human_problem_sub_cause
        self.emergency_vehicle_approaching_sub_cause = emergency_vehicle_approaching_sub_cause
        self.hazardous_location_dangerous_curve_sub_cause = hazardous_location_dangerous_curve_sub_cause
        self.hazardous_location_surface_condition_sub_cause = hazardous_location_surface_condition_sub_cause
        self.hazardous_location_obstacle_on_the_road_sub_cause = hazardous_location_obstacle_on_the_road_sub_cause
        self.hazardous_location_animal_on_the_road_sub_cause = hazardous_location_animal_on_the_road_sub_cause
        self.collision_risk_sub_cause = collision_risk_sub_cause
        self.signal_violation_sub_cause = signal_violation_sub_cause
        self.rescue_and_recovery_work_in_progress_sub_cause = rescue_and_recovery_work_in_progress_sub_cause
        self.dangerous_end_of_queue_sub_cause = dangerous_end_of_queue_sub_cause
        self.dangerous_situation_sub_cause = dangerous_situation_sub_cause
        self.vehicle_break_down_sub_cause = vehicle_break_down_sub_cause
        self.post_crash_sub_cause = post_crash_sub_cause

    def __str__(self):
        pass