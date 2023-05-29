class CamData:
    def __init__(self, cam_key, time_key, segment_key, station_id, latitude, longitude, altitude, speed, heading,
                 acceleration, station_type, vehicle_role, time_stamp, type_of_fuel, brake_pedal_engaged,
                 gas_pedal_engaged, emergency_pedal_engaged, collision_warning_engaged, acc_engaged,
                 cruise_control_engaged, speed_limiter_engaged, stationary_since):
        self.cam_key = cam_key
        self.time_key = time_key
        self.segment_key = segment_key
        self.station_id = station_id
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.speed = speed
        self.heading = heading
        self.acceleration = acceleration
        self.station_type = station_type
        self.vehicle_role = vehicle_role
        self.time_stamp = time_stamp
        self.type_of_fuel = type_of_fuel
        self.brake_pedal_engaged = brake_pedal_engaged
        self.gas_pedal_engaged = gas_pedal_engaged
        self.emergency_pedal_engaged = emergency_pedal_engaged
        self.collision_warning_engaged = collision_warning_engaged
        self.acc_engaged = acc_engaged
        self.cruise_control_engaged = cruise_control_engaged
        self.speed_limiter_engaged = speed_limiter_engaged
        self.stationary_since = stationary_since

class RoadEventData:
    def __init__(self, road_event_key, description, severity, status, impact_level):
        self.road_event_key = road_event_key
        self.description = description
        self.severity = severity
        self.status = status
        self.impact_level = impact_level

class DenmData:
    def __init__(self, denm_key, road_event_key, time_key, heading, time_stamp, longitude, latitude, altitude, cause, sub_cause,traffic_cause,road_works_sub_cause, accident_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_sub_cause, human_problem_sub_cause, collision_risk_sub_cause, dangerous_situation_sub_cause, vehicle_break_down_sub_cause, post_crash_sub_cause, human_presence_on_the_road_sub_cause, adverse_weather_condition_extreme_weather_condition_sub_cause, adverse_weather_condition_adhesion_sub_cause, adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause, emergency_vehicle_approaching_sub_cause, hazardous_location_surface_condition_sub_cause, hazardous_location_obstacle_on_the_road_sub_cause, hazardous_location_animal_on_the_road_sub_cause, rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause, wrong_way_driving_sub_cause, hazardous_location_dangerous_curve_sub_cause,signal_violation_sub_cause):
        self.denm_key = denm_key
        self.road_event_key = road_event_key
        self.time_key = time_key
        self.heading = heading
        self.time_stamp = time_stamp
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.cause = cause
        self.sub_cause = sub_cause
        self.traffic_cause = traffic_cause
        self.road_works_sub_cause = road_works_sub_cause
        self.accident_sub_cause = accident_sub_cause
        self.slow_vehicle_sub_cause = slow_vehicle_sub_cause
        self.stationary_vehicle_sub_cause = stationary_vehicle_sub_cause
        self.human_problem_sub_cause = human_problem_sub_cause
        self.collision_risk_sub_cause = collision_risk_sub_cause
        self.dangerous_situation_sub_cause = dangerous_situation_sub_cause
        self.vehicle_break_down_sub_cause = vehicle_break_down_sub_cause
        self.post_crash_sub_cause = post_crash_sub_cause
        self.human_presence_on_the_road_sub_cause = human_presence_on_the_road_sub_cause
        self.adverse_weather_condition_extreme_weather_condition_sub_cause = adverse_weather_condition_extreme_weather_condition_sub_cause
        self.adverse_weather_condition_adhesion_sub_cause = adverse_weather_condition_adhesion_sub_cause
        self.adverse_weather_condition_visibility_sub_cause = adverse_weather_condition_visibility_sub_cause
        self.adverse_weather_condition_precipitation_sub_cause = adverse_weather_condition_precipitation_sub_cause
        self.emergency_vehicle_approaching_sub_cause = emergency_vehicle_approaching_sub_cause
        self.hazardous_location_surface_condition_sub_cause =hazardous_location_surface_condition_sub_cause
        self.hazardous_location_obstacle_on_the_road_sub_cause = hazardous_location_obstacle_on_the_road_sub_cause
        self.hazardous_location_animal_on_the_road_sub_cause = hazardous_location_animal_on_the_road_sub_cause
        self.rescue_and_recovery_work_in_progress_sub_cause = rescue_and_recovery_work_in_progress_sub_cause
        self.dangerous_end_of_queue_sub_cause = dangerous_end_of_queue_sub_cause
        self.wrong_way_driving_sub_cause = wrong_way_driving_sub_cause
        self.hazardous_location_dangerous_curve_sub_cause = hazardous_location_dangerous_curve_sub_cause
        self.signal_violation_sub_cause = signal_violation_sub_cause

class RoadData:
    def __init__(self, road_key, road_name, road_type, road_length, number_of_lanes, start_point, end_point):
        self.road_key = road_key
        self.road_name = road_name
        self.road_type = road_type
        self.road_length = road_length
        self.number_of_lanes = number_of_lanes
        self.start_point = start_point
        self.end_point = end_point

class SegmentData:
    def __init__(self, segment_key, road_key, segment_name, segment_type, segment_length, number_of_lanes, start_point, end_point):
        self.segment_key = segment_key
        self.road_key = road_key
        self.segment_name = segment_name
        self.segment_type = segment_type
        self.segment_length = segment_length
        self.number_of_lanes = number_of_lanes
        self.start_point = start_point
        self.end_point = end_point

class ZoneData:
    def __init__(self, zone_key, zone_name, zone_type, zone_description, zone_area):
        self.zone_key = zone_key
        self.zone_name = zone_name
        self.zone_type = zone_type
        self.zone_description = zone_description
        self.zone_area = zone_area

class RoadSignData:
    def __init__(self, road_sign_key, road_description, code, symbol, class_code, visibility):
        self.road_sign_key = road_sign_key
        self.road_description = road_description
        self.code = code
        self.symbol = symbol
        self.class_code = class_code
        self.visibility = visibility


class IvimData:
    def __init__(self, ivim_key, zone_key, road_sign_key, latitude, longitude, altitude):
        self.ivim_key = ivim_key
        self.zone_key = zone_key
        self.road_sign_key = road_sign_key
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

class EventData:
    def __init__(self, event_key, designation, start_time, end_time, flag_single_day_event):
        self.event_key = event_key
        self.designation = designation
        self.start_time = start_time
        self.end_time = end_time
        self.flag_single_day_event = flag_single_day_event

class TimeData:
    def __init__(self, time_key, event_key, day, month, year, is_weekend_day, is_holiday, trimester, semester, week_day_number, week_day_name, season, full_date_description):
        self.time_key = time_key
        self.event_key = event_key
        self.day = day
        self.month = month
        self.year = year
        self.is_weekend_day = is_weekend_day
        self.is_holiday = is_holiday
        self.trimester = trimester
        self.semester = semester
        self.week_day_number = week_day_number
        self.week_day_name = week_day_name
        self.season = season
        self.full_date_description = full_date_description