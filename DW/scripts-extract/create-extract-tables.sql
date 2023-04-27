-- Database: projeto-informatico
CREATE TABLE t_ext_road_event
(
	road_event_key VARCHAR(50) PRIMARY KEY,
	description VARCHAR(100) NOT NULL,
	severity VARCHAR(10) NOT NULL,
	status VARCHAR(10) NOT NULL,
	impact VARCHAR(10) NOT NULL,
	cause VARCHAR(50) NOT NULL,
	sub_cause VARCHAR(50) NOT NULL,
	traffic_cause VARCHAR(50) NOT NULL,
	accident_sub_cause VARCHAR(50) NOT NULL,
	road_works_sub_cause VARCHAR(50) NOT NULL,
	slow_vehicle_sub_cause VARCHAR(50) NOT NULL,
	stationary_vehicle_cause VARCHAR(50) NOT NULL,
	human_problem_sub_cause VARCHAR(50) NOT NULL,
	collision_risk_sub_cause VARCHAR(50) NOT NULL,
	dangerous_situation_sub_cause VARCHAR(50) NOT NULL,
	human_presence_on_the_road_sub_cause VARCHAR(50) NOT NULL,
	adverse_weather_condition_extreme_weather_condition_sub_cause VARCHAR(50) NOT NULL,
	adverse_weather_condition_adhesion_sub_cause VARCHAR(50) NOT NULL,
	adverse_weather_condition_visibility_sub_cause VARCHAR(50) NOT NULL,
	adverse_weather_condition_precipitation_sub_cause VARCHAR(50) NOT NULL,
	emergency_vehicle_approaching_sub_cause VARCHAR(50) NOT NULL,
	hazardous_location_surface_condition_sub_cause VARCHAR(50) NOT NULL,
	hazardous_location_obstacle_on_the_road_sub_cause VARCHAR(50) NOT NULL,
	hazardous_location_animal_on_the_road_sub_cause VARCHAR(50) NOT NULL,
	rescue_and_recovery_work_in_progress_sub_cause VARCHAR(50) NOT NULL,
	dangerous_end_of_queue_sub_cause VARCHAR(50) NOT NULL,
	vehicle_break_down_sub_cause VARCHAR(50) NOT NULL,
	post_crash_sub_cause VARCHAR(50) NOT NULL
);

CREATE TABLE t_ext_cam
(
	cam_key INT PRIMARY KEY,
	time_key INT NOT NULL,
	c_location POINT NOT NULL,
	speed INT NOT NULL,
	heading INT NOT NULL,
	acceleration INT NOT NULL,
	station_type VARCHAR(20) NOT NULL,
	vehicle_role VARCHAR(20) NOT NULL,
	time_stamp VARCHAR(12) NOT NULL,
	class_dangerous_cargo VARCHAR(20) NOT NULL,
	fuel_type VARCHAR(20) NOT NULL,
	brake_pedal_engaged BOOLEAN NOT NULL,
	gas_pedal_engaged BOOLEAN NOT NULL,
	emergency_pedal_engaged BOOLEAN NOT NULL,
	collision_warning_engaged BOOLEAN NOT NULL,
	speed_limiter_engaged BOOLEAN NOT NULL,
	cruise_control_engaged BOOLEAN NOT NULL,
	stationary_since VARCHAR(20) NOT NULL
); 

CREATE TABLE t_ext_denm
(
	denm_key SERIAL PRIMARY KEY,
	time_key INT NOT NULL,
	road_event_key VARCHAR(50) NOT NULL,
	time_stamp VARCHAR(12) NOT NULL,
	c_location POINT NOT NULL,
	heading INT NOT NULL,
	confidence_level VARCHAR(20) NOT NULL,
	source_id INT NOT NULL,
	destination_id INT NOT NULL,
	FOREIGN KEY (road_event_key) REFERENCES t_dim_road_event (road_event_key)
);
