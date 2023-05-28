INSERT INTO t_event (designation, start_time, end_time, flag_single_day_event)
VALUES ('Event 1', 10.5, 12.0, TRUE),
       ('Event 2', 14.0, 16.5, FALSE),
       ('Event 3', 9.0, 11.5, TRUE),
       ('Event 4', 13.5, 15.0, FALSE),
       ('Event 5', 11.0, 12.5, TRUE),
       ('Event 6', 15.0, 16.5, FALSE),
       ('Event 7', 9.5, 11.0, TRUE),
       ('Event 8', 13.0, 14.5, FALSE),
       ('Event 9', 12.0, 13.5, TRUE),
       ('Event 10', 14.5, 16.0, FALSE);

INSERT INTO t_zone (zone_name, zone_type, zone_description, zone_area)
VALUES ('Zone 1', 'Type 1', 'Description 1', 'Area 1'),
       ('Zone 2', 'Type 2', 'Description 2', 'Area 2'),
       ('Zone 3', 'Type 3', 'Description 3', 'Area 3'),
       ('Zone 4', 'Type 4', 'Description 4', 'Area 4'),
       ('Zone 5', 'Type 5', 'Description 5', 'Area 5'),
       ('Zone 6', 'Type 6', 'Description 6', 'Area 6'),
       ('Zone 7', 'Type 7', 'Description 7', 'Area 7'),
       ('Zone 8', 'Type 8', 'Description 8', 'Area 8'),
       ('Zone 9', 'Type 9', 'Description 9', 'Area 9'),
       ('Zone 10', 'Type 10', 'Description 10', 'Area 10');
       
INSERT INTO t_road (road_name, road_type, road_length, number_of_lanes, start_point, end_point)
VALUES ('Road 1', 'Type 1', 1000, 2, 0.0, 100.0),
       ('Road 2', 'Type 2', 1500, 3, 50.0, 200.0),
       ('Road 3', 'Type 1', 800, 2, 20.0, 120.0),
       ('Road 4', 'Type 3', 2000, 4, 0.0, 200.0),
       ('Road 5', 'Type 2', 1200, 2, 30.0, 150.0),
       ('Road 6', 'Type 1', 1800, 3, 100.0, 300.0),
       ('Road 7', 'Type 3', 500, 1, 50.0, 100.0),
       ('Road 8', 'Type 2', 1600, 2, 80.0, 240.0),
       ('Road 9', 'Type 1', 900, 2, 10.0, 110.0),
       ('Road 10', 'Type 3', 1400, 3, 70.0, 210.0);
       
INSERT INTO t_road_event (description, severity, status, impact_level)
VALUES
    ('Road event 1', 'Low', 'Active', 'Minor'),
    ('Road event 2', 'Medium', 'Active', 'Moderate'),
    ('Road event 3', 'High', 'Active', 'Significant'),
    ('Road event 4', 'Low', 'Resolved', 'Minor'),
    ('Road event 5', 'Medium', 'Active', 'Moderate'),
    ('Road event 6', 'High', 'Active', 'Significant'),
    ('Road event 7', 'Medium', 'Resolved', 'Moderate'),
    ('Road event 8', 'High', 'Active', 'Significant'),
    ('Road event 9', 'Low', 'Active', 'Minor'),
    ('Road event 10', 'Medium', 'Resolved', 'Moderate');	   
	   
INSERT INTO t_segment (road_key, segment_name, segment_type, segment_length, number_of_lanes, start_point, end_point)
VALUES (41, 'Segment 1', 'Type 1', 200, 2, 0.0, 50.0),
       (42, 'Segment 2', 'Type 2', 300, 3, 50.0, 100.0),
       (43, 'Segment 1', 'Type 1', 250, 2, 50.0, 100.0),
       (44, 'Segment 2', 'Type 2', 350, 3, 100.0, 150.0),
       (45, 'Segment 1', 'Type 1', 150, 2, 20.0, 50.0),
       (46, 'Segment 2', 'Type 2', 250, 3, 50.0, 90.0),
       (47, 'Segment 1', 'Type 1', 400, 4, 0.0, 100.0),
       (48, 'Segment 2', 'Type 2', 600, 4, 100.0, 200.0),
       (49, 'Segment 1', 'Type 1', 180, 2, 30.0, 60.0),
       (50, 'Segment 2', 'Type 2', 280, 3, 60.0, 100.0);

INSERT INTO t_time (event_key, c_day, c_month, c_year, weekend_day, week_day_number, week_day_name, is_holiday, trimester, semester, season, full_date_description)
VALUES (51, 1, 1, 2023, TRUE, 1, 'Monday', FALSE, 1, 1, 'Winter', 'January 1, 2023'),
       (52, 5, 2, 2023, FALSE, 5, 'Friday', FALSE, 1, 1, 'Winter', 'February 5, 2023'),
       (53, 15, 3, 2023, FALSE, 2, 'Tuesday', FALSE, 1, 1, 'Winter', 'March 15, 2023'),
       (54, 20, 4, 2023, FALSE, 6, 'Saturday', TRUE, 2, 1, 'Spring', 'April 20, 2023'),
       (55, 10, 5, 2023, TRUE, 4, 'Thursday', FALSE, 2, 1, 'Spring', 'May 10, 2023'),
       (56, 22, 6, 2023, FALSE, 2, 'Tuesday', FALSE, 2, 2, 'Summer', 'June 22, 2023'),
       (57, 5, 7, 2023, FALSE, 5, 'Friday', FALSE, 2, 2, 'Summer', 'July 5, 2023'),
       (58, 18, 8, 2023, TRUE, 3, 'Wednesday', FALSE, 3, 2, 'Summer', 'August 18, 2023'),
       (59, 1, 9, 2023, TRUE, 6, 'Saturday', TRUE, 3, 2, 'Fall', 'September 1, 2023'),
       (60, 14, 10, 2023, FALSE, 4, 'Thursday', FALSE, 3, 2, 'Fall', 'October 14, 2023');

INSERT INTO t_road_sign (road_sign_key, road_sign_description, road_sign_code, road_sign_symbol, road_sign_class, road_sign_visibility)
VALUES
    ('RS001', 'Stop Sign', 'STP001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS002', 'No Parking', 'NPK001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS003', 'Speed Limit 50', 'SL050', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS004', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS005', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS006', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS007', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS008', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS009', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible'),
    ('RS00', 'Yield Sign', 'YLD001', '\\x89504E470D0A1A0A0000000D4948445200000028000000280806000000C4BFC7000000017352474200AECE1CE90000000467414D410000B18F0BFC6105000000097048597300000EC300000EC301C76FA86400000E2217457CF58600000E2219EDDDA33400000613465624B47440000A4B8EEF24742000000E229494441543B2E7C88409CEA'
        , 'Regulatory', 'Visible');
		
INSERT INTO t_cam (time_key, segment_key, station_id, latitude, longitude, altitude, speed, heading, acceleration, station_type, vehicle_role, time_stamp, fuel_type, acceleration_control, stationary_since)
VALUES
    (1, 71, 1001, 123456, 789012, 100, 60, 90, 5, 1, 1, 1621456789, '0100', '0000', 0),
    (2, 72, 1002, 234567, 890123, 200, 55, 120, 3, 2, 2, 1621456790, '0101', '0001', NULL),
    (3, 73, 1003, 345678, 901234, 150, 70, 180, 2, 1, 1, 1621456791, '0100', '0101', NULL),
    (4, 74, 1004, 456789, 012345, 180, 65, 270, 4, 2, 2, 1621456792, '0101', '0011', NULL),
    (5, 75, 1005, 567890, 123456, 120, 50, 45, 1, 1, 1, 1621456793, '0100', '0001', NULL),
    (6, 76, 1006, 678901, 234567, 220, 75, 150, 3, 2, 2, 1621456794, '0101', '0110', NULL),
    (7, 77, 1007, 789012, 345678, 170, 80, 225, 2, 1, 1, 1621456795, '0100', '0011', NULL),
    (8, 78, 1008, 890123, 456789, 200, 70, 315, 4, 2, 2, 1621456796, '0101', '0100', NULL),
    (9, 79, 1009, 901234, 567890, 140, 45, 90, 1, 1, 1, 1621456797, '0100', '0000', 1),
    (10, 80, 1010, 012345, 678901, 240, 80, 180, 3, 2, 2, 1621456798, '0101', '0010', NULL);

INSERT INTO t_denm (time_key, road_event_key, time_stamp, latitude, longitude, altitude, heading, cause, sub_cause, traffic_cause, accident_sub_cause_code, road_works_sub_cause, accident_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_cause, human_problem_sub_cause, collision_risk_sub_cause, dangerous_situation_sub_cause, vehicle_break_down_sub_cause, post_crash_sub_cause, human_presence_on_the_road_sub_cause, adverse_weather_condition_extreme_weather_condition_sub_cause, adverse_weather_condition_adhesion_sub_cause, adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause, emergency_vehicle_approaching_sub_cause, hazardous_location_surface_condition_sub_cause, hazardous_location_obstacle_on_the_road_sub_cause, hazardous_location_animal_on_the_road_sub_cause, rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause)
VALUES
    (1, 1, 1621456789, 123456, 789012, 100, 90, 1, 1, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
    (2, 2, 1621456790, 234567, 890123, 200, 120, 2, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
    (3, 3, 1621456791, 345678, 901234, 150, 180, 3, 1, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
    (4, 4, 1621456792, 456789, 012345, 180, 270, 5, 2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
    (5, 5, 1621456793, 567890, 123456, 120, 45, 2, 2, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
    (6, 6, 1621456794, 678901, 234567, 220, 150, 3, 3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
    (7, 7, 1621456795, 789012, 345678, 170, 225, 2, 3, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    (8, 8, 1621456796, 789012, 345678, 170, 225, 26, 3, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    (9, 9, 1621456797, 789012, 345678, 170, 225, 92, 3, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    (10, 10, 1621456798, 789012, 345678, 170, 225, 91, 3, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
	 
INSERT INTO t_ivim (zone_key, road_sign_key, latitude, longitude, altitude)
VALUES
    (51, 'RS00', 123456, 789012, 100),
    (52, 'RS001', 234567, 890123, 200),
    (53, 'RS002', 345678, 901234, 150),
    (54, 'RS003', 456789, 012345, 180),
    (55, 'RS004', 567890, 123456, 120),
    (56, 'RS005', 678901, 234567, 220),
    (57, 'RS006', 789012, 345678, 170),
    (58, 'RS007', 890123, 456789, 200),
    (59, 'RS008', 901234, 567890, 140),
    (60, 'RS009', 012345, 678901, 240);