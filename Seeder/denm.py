import random
import sys
import psycopg2
from psycopg2 import Error

import constants
import event
import timeClass
import roadEvent

def insert_data_to_database(data):
    try:
        connection = psycopg2.connect(
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port,
            database=constants.db_name
        )

        cursor = connection.cursor()

        cursor.execute("SELECT MAX(denm_key), MAX(time_key), MAX(road_event_key) FROM t_denm")
        max_values = cursor.fetchone()
        max_denm_key = max_values[0]
        max_time_key = max_values[1]
        max_road_event_key = max_values[2]

        if max_denm_key is None:
            max_denm_key = 0
        if max_time_key is None:
            max_time_key = 0
        if max_road_event_key is None:
            max_road_event_key = 0

        # Modify the SQL INSERT statement based on your table structure and column names
        insert_query = """
            INSERT INTO t_denm (
                denm_key, time_key, road_event_key, time_stamp, latitude, longitude, altitude, heading, cause, traffic_sub_cause,
                road_works_sub_cause, accident_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_sub_cause,
                human_problem_sub_cause, collision_risk_sub_cause, dangerous_situation_sub_cause,
                vehicle_break_down_sub_cause, post_crash_sub_cause, human_presence_on_the_road_sub_cause,
                adverse_weather_condition_extreme_weather_condition_sub_cause, adverse_weather_condition_adhesion_sub_cause,
                adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause,
                emergency_vehicle_approaching_sub_cause, hazardous_location_dangerous_curve_sub_cause, hazardous_location_surface_condition_sub_cause,
                hazardous_location_obstacle_on_the_road_sub_cause, hazardous_location_animal_on_the_road_sub_cause,
                rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause, signal_violation_sub_cause, wrong_way_driving_sub_cause
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for record in data:
            max_denm_key += 1
            max_time_key += 1
            max_road_event_key += 1
            record['denm_key'] = max_denm_key
            record['time_key'] = max_time_key
            record['road_event_key'] = max_road_event_key

            denm_key = record['denm_key']
            time_key = record['time_key']
            road_event_key = record['road_event_key']
            time_stamp = record['time_stamp']
            latitude = record['latitude']
            longitude = record['longitude']
            altitude = record['altitude']
            heading = record['heading']
            cause = record['cause']
            traffic_sub_cause = record['traffic_sub_cause']
            road_works_sub_cause = record['road_works_sub_cause']
            accident_sub_cause = record['accident_sub_cause']
            slow_vehicle_sub_cause = record['slow_vehicle_sub_cause']
            stationary_vehicle_sub_cause = record['stationary_vehicle_sub_cause']
            human_problem_sub_cause = record['human_problem_sub_cause']
            collision_risk_sub_cause = record['collision_risk_sub_cause']
            dangerous_situation_sub_cause = record['dangerous_situation_sub_cause']
            vehicle_break_down_sub_cause = record['vehicle_break_down_sub_cause']
            adverse_weather_condition_extreme_weather_condition_sub_cause = record['adverse_weather_condition_extreme_weather_condition_sub_cause']
            adverse_weather_condition_adhesion_sub_cause = record['adverse_weather_condition_adhesion_sub_cause']
            adverse_weather_condition_visibility_sub_cause = record['adverse_weather_condition_visibility_sub_cause']
            adverse_weather_condition_precipitation_sub_cause = record['adverse_weather_condition_precipitation_sub_cause']
            emergency_vehicle_approaching_sub_cause = record['emergency_vehicle_approaching_sub_cause']
            hazardous_location_dangerous_curve_sub_cause = record['hazardous_location_dangerous_curve_sub_cause']
            hazardous_location_surface_condition_sub_cause = record['hazardous_location_surface_condition_sub_cause']
            hazardous_location_obstacle_on_the_road_sub_cause = record['hazardous_location_obstacle_on_the_road_sub_cause']
            hazardous_location_animal_on_the_road_sub_cause = record['hazardous_location_animal_on_the_road_sub_cause']
            rescue_and_recovery_work_in_progress_sub_cause = record['rescue_and_recovery_work_in_progress_sub_cause']
            dangerous_end_of_queue_sub_cause = record['dangerous_end_of_queue_sub_cause']
            signal_violation_sub_cause = record['signal_violation_sub_cause']
            wrong_way_driving_sub_cause = record['wrong_way_driving_sub_cause']
            post_crash_sub_cause = record['post_crash_sub_cause']
            human_presence_on_the_road_sub_cause = record['human_presence_on_the_road_sub_cause']

            if cause == 1: #traffic condition
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 2: #accident
                traffic_sub_cause = None
                road_works_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 3: #road works
                traffic_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 6: #adverse weather condition - adhesion
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 9: #hazardous location - surface condition
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 10:  # hazardous location obstacle on the road
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 11:  # hazardous location animal on the road
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 12:  # human presence on the road
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 14:  # wrong way driving
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
            elif cause == 15:  # rescue and recovery work in progress
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 17:  # adverse weather condition - extreme weather condition
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 18:  # adverse weather condition - visibility
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 19:  # adverse weather condition - precipitation
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 26:  # slow vehicle
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 27:  # dangerous end of queue
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 91:  # vehicle break down
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 92:  # post crash
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 93:  # human problem
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 94:  # stationary vehicle
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 95:  # emergency vehicle approaching
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 96:  # hazardous location - dangerous curve
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 97:  # collision risk
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                human_problem_sub_cause = None
                stationary_vehicle_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 98:  # signal violation
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                dangerous_situation_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                wrong_way_driving_sub_cause = None
            elif cause == 99:  # dangerous situation
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
            else:
                traffic_sub_cause = None
                road_works_sub_cause = None
                accident_sub_cause = None
                slow_vehicle_sub_cause = None
                stationary_vehicle_sub_cause = None
                human_problem_sub_cause = None
                collision_risk_sub_cause = None
                vehicle_break_down_sub_cause = None
                post_crash_sub_cause = None
                human_presence_on_the_road_sub_cause = None
                adverse_weather_condition_extreme_weather_condition_sub_cause = None
                adverse_weather_condition_adhesion_sub_cause = None
                adverse_weather_condition_visibility_sub_cause = None
                adverse_weather_condition_precipitation_sub_cause = None
                emergency_vehicle_approaching_sub_cause = None
                hazardous_location_dangerous_curve_sub_cause = None
                hazardous_location_surface_condition_sub_cause = None
                hazardous_location_obstacle_on_the_road_sub_cause = None
                hazardous_location_animal_on_the_road_sub_cause = None
                rescue_and_recovery_work_in_progress_sub_cause = None
                signal_violation_sub_cause = None
                wrong_way_driving_sub_cause = None
                dangerous_end_of_queue_sub_cause = None
                dangerous_situation_sub_cause = None

            values = (
                denm_key,
                time_key,
                road_event_key,
                time_stamp,
                latitude,
                longitude,
                altitude,
                heading,
                cause,
                traffic_sub_cause,
                road_works_sub_cause,
                accident_sub_cause,
                slow_vehicle_sub_cause,
                stationary_vehicle_sub_cause,
                human_problem_sub_cause,
                collision_risk_sub_cause,
                dangerous_situation_sub_cause,
                vehicle_break_down_sub_cause,
                post_crash_sub_cause,
                human_presence_on_the_road_sub_cause,
                adverse_weather_condition_extreme_weather_condition_sub_cause,
                adverse_weather_condition_adhesion_sub_cause,
                adverse_weather_condition_visibility_sub_cause,
                adverse_weather_condition_precipitation_sub_cause,
                emergency_vehicle_approaching_sub_cause,
                hazardous_location_dangerous_curve_sub_cause,
                hazardous_location_surface_condition_sub_cause,
                hazardous_location_obstacle_on_the_road_sub_cause,
                hazardous_location_animal_on_the_road_sub_cause,
                rescue_and_recovery_work_in_progress_sub_cause,
                dangerous_end_of_queue_sub_cause,
                signal_violation_sub_cause,
                wrong_way_driving_sub_cause
            )

            cursor.execute(insert_query, values)

        connection.commit()
        print("Denm Data inserted successfully!")

    except (Exception, Error) as error:
        print("Error while inserting data into PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

class Denm:
    def __init__(self, property_ranges):
        self.property_ranges = property_ranges
        self.current_denm_key = property_ranges.get("denm_key", [])[1] - 1  # Initialize with the previous value
        self.current_road_event_key = property_ranges.get("road_event_key", [])[1] - 1  # Initialize with the previous value
        self.current_time_key = property_ranges.get("time_key", [])[1] - 1  # Initialize with the previous value

    def generate_random_data(self):
        generated_data = {}

        for property_name, value_range in self.property_ranges.items():
            if property_name == "denm_key":
                self.current_denm_key += 1  # Increment the zone_key value
                generated_data[property_name] = self.current_denm_key
            elif property_name == "road_event_key":
                self.current_road_event_key += 1
                generated_data[property_name] = self.current_road_event_key
            elif property_name == "time_key":
                self.current_time_key += 1
                generated_data[property_name] = self.current_time_key
            else:
                generated_data[property_name] = self.generate_value(value_range)

        return generated_data

    @staticmethod
    def generate_value(value_range):
        value_type = value_range[0]

        if value_type == "int":
            min_value, max_value = value_range[1:]
            return random.randint(min_value, max_value)
        elif value_type == "float":
            min_value, max_value = value_range[1:]
            return random.uniform(min_value, max_value)
        elif value_type == "choice":
            choices = value_range[1:]
            return random.choice(choices)
        else:
            return None

    def generate_seeders(self, n):
        seeders = []
        for _ in range(n):
            seeder = Denm(self.property_ranges)
            seeders.append(seeder)
        return seeders

    def insert_data_to_database(self):
        data = self.generate_random_data()
        insert_data_to_database([data])

property_ranges = {
    "denm_key": ["int", 1, sys.maxsize],
    "road_event_key": ["int", 1, sys.maxsize],
    "time_key": ["int", 1, sys.maxsize],
    "heading": ["int", 0, 3601],
    "time_stamp": ["int", 0, 4398046511103],
    "longitude": ["int", -1800000000, 1800000000],
    "latitude": ["int", -900000000, 900000000],
    "altitude": ["int", -100000, 100000],
    "cause": ["int", 0, 99],
    "traffic_sub_cause": ["int", 0, 8],
    "accident_sub_cause": ["int", 0, 8],
    "road_works_sub_cause" : ["int", 0, 6],
    "human_presence_on_the_road_sub_cause": ["int", 0, 3],
    "wrong_way_driving_sub_cause": ["int", 0, 2],
    "adverse_weather_condition_extreme_weather_condition_sub_cause": ["int", 0, 6],
    "adverse_weather_condition_adhesion_sub_cause": ["int", 0, 10],
    "adverse_weather_condition_visibility_sub_cause": ["int", 0, 8],
    "adverse_weather_condition_precipitation_sub_cause": ["int", 0, 3],
    "slow_vehicle_sub_cause": ["int", 0, 8],
    "stationary_vehicle_sub_cause": ["int", 0, 5],
    "human_problem_sub_cause": ["int", 0, 2],
    "emergency_vehicle_approaching_sub_cause": ["int", 0, 2],
    "hazardous_location_dangerous_curve_sub_cause": ["int", 0, 5],
    "hazardous_location_surface_condition_sub_cause": ["int", 0, 9],
    "hazardous_location_obstacle_on_the_road_sub_cause": ["int", 0, 7],
    "hazardous_location_animal_on_the_road_sub_cause": ["int", 0, 4],
    "collision_risk_sub_cause": ["int", 0, 4],
    "signal_violation_sub_cause": ["int", 0, 3],
    "rescue_and_recovery_work_in_progress_sub_cause": ["int", 0, 5],
    "dangerous_end_of_queue_sub_cause": ["int", 0, 4],
    "dangerous_situation_sub_cause": ["int", 0, 7],
    "vehicle_break_down_sub_cause": ["int", 0, 9],
    "post_crash_sub_cause": ["int", 0, 4],
}

def main():
    # Create a Seeder instance
    seeder = Denm(property_ranges)

    # Generate and print example data
    for _ in range(1):
        seeder.insert_data_to_database()

main()

"""
data = seeder.generate_random_data()
print(data)
print("---")
"""