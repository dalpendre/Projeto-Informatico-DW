INSERT INTO t_dim_time (c_day, c_month, c_year, c_week_day, c_is_holiday, c_trimester, c_semester)
VALUES
(1, 1, 2023, 'Sunday', true, 1, 1),
(2, 1, 2023, 'Monday', false, 1, 1),
(3, 1, 2023, 'Tuesday', false, 1, 1),
(4, 1, 2023, 'Wednesday', false, 1, 1),
(5, 1, 2023, 'Thursday', false, 1, 1),
(6, 1, 2023, 'Friday', false, 1, 1),
(7, 1, 2023, 'Saturday', false, 1, 1),
(8, 1, 2023, 'Sunday', false, 1, 1),
(9, 1, 2023, 'Monday', false, 1, 1),
(10, 1, 2023, 'Tuesday', false, 1, 1);

INSERT INTO t_fact_cam 
(
    cam_key, time_key, c_location, speed, heading, acceleration, 
    station_type, vehicle_role, time_stamp, class_dangerous_cargo, 
    fuel_type, brake_pedal_engaged, gas_pedal_engaged, 
    emergency_pedal_engaged, collision_warning_engaged, speed_limiter_engaged, 
    cruise_control_engaged, stationary_since
)
VALUES
(1, 21, POINT(12.34, 56.78), 80, 45, 2, 'Station', 'Bus', '202301011200', 'None', 'Gasoline', false, true, false, false, true, false, '202301011100'),
(2, 22, POINT(23.45, 67.89), 70, 90, 0, 'Station', 'Truck', '202301011215', 'Explosives', 'Diesel', false, false, true, false, false, true, '202301011200'),
(3, 23, POINT(34.56, 78.90), 60, 180, 1, 'Station', 'Car', '202301011230', 'None', 'Electric', true, false, false, true, false, false, '202301011215'),
(4, 24, POINT(45.67, 89.01), 50, 270, 0, 'Station', 'Motorcycle', '202301011245', 'Flammable Gas', 'Gasoline', true, false, true, false, true, true, '202301011230'),
(5, 25, POINT(56.78, 90.12), 40, 0, 1, 'Station', 'Bus', '202301011300', 'None', 'Diesel', false, true, false, true, false, false, '202301011245'),
(6, 26, POINT(67.89, 12.34), 30, 90, 2, 'Station', 'Car', '202301011315', 'Explosives', 'Electric', false, false, true, false, true, true, '202301011300'),
(7, 27, POINT(78.90, 23.45), 20, 180, 0, 'Station', 'Truck', '202301011330', 'None', 'Gasoline', true, false, false, true, false, false, '202301011315'),
(8, 28, POINT(89.01, 34.56), 10, 270, 1, 'Station', 'Motorcycle', '202301011345', 'Flammable Gas', 'Diesel', false, true, false, false, true, true, '202301011330'),
(9, 29, POINT(90.12, 45.67), 5, 0, 0, 'Station', 'Bus', '202301011400', 'None', 'Electric', true, false, true, false, false, false, '202301011345'),
(10, 30, POINT(12.34, 56.78), 0, 90, 2, 'Station', 'Car', '202301011415', 'Explosives', 'Gasoline', false, false, false, true, true, true, '202301011400');

SELECT * FROM t_fact_cam;