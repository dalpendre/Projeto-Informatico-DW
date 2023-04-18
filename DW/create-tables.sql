-- Database: projeto_informatico

CREATE TABLE t_dim_road_event
(
	road_event_key VARCHAR(50) PRIMARY KEY,
	description VARCHAR(100) NOT NULL,
	severity VARCHAR(10) NOT NULL
);

CREATE TABLE t_dim_vehicle
(
	vehicle_key INT PRIMARY KEY,
	vehicle_type VARCHAR(20) NOT NULL,
	vehicle_class VARCHAR(20) NOT NULL,
	road_event_key VARCHAR(50) NOT NULL,
	FOREIGN KEY (road_event_key) REFERENCES t_dim_road_event (road_event_key)
);

CREATE TABLE t_dim_road_sign
(
	road_sign_key VARCHAR(10) PRIMARY KEY,
	road_sign_description VARCHAR(50) NOT NULL
);

CREATE TABLE t_dim_road
(
	road_key VARCHAR(10) PRIMARY KEY,
	speed_limit INT NOT NULL
);

CREATE TABLE t_dim_date
(
	date_key SERIAL PRIMARY KEY,
	c_day INT NOT NULL,
	c_month INT NOT NULL,
	c_year INT NOT NULL
);

CREATE TABLE t_dim_time
(
	date_key SERIAL PRIMARY KEY,
	c_hour INT NOT NULL,
	minutes INT NOT NULL,
	seconds INT NOT NULL
);

CREATE TABLE t_fact_vehicle_in_circulation
(
	vehicle_in_circulation_key INT PRIMARY KEY,
	vehicle_key INT NOT NULL,
	date_key INT NOT NULL,
	time_key INT NOT NULL,
	road_key VARCHAR(10) NOT NULL,
	c_location POINT NOT NULL,
	speed INT NOT NULL,
	heading INT NOT NULL,
	acceleration INT NOT NULL,
	FOREIGN KEY (vehicle_key) REFERENCES t_dim_vehicle (vehicle_key),
	FOREIGN KEY (date_key) REFERENCES t_dim_date (date_key),
	FOREIGN KEY (time_key) REFERENCES t_dim_time (time_key),
	FOREIGN KEY (road_key) REFERENCES t_dim_road (road_key)
); 

CREATE TABLE t_fact_road_event
(
	road_event_key SERIAL PRIMARY KEY,
	vehicle_key INT NOT NULL,
	date_key INT NOT NULL,
	time_key INT NOT NULL,
	road_key VARCHAR(10) NOT NULL,
	road_event_key VARCHAR(50) NOT NULL,
	FOREIGN KEY (vehicle_key) REFERENCES t_dim_vehicle (vehicle_key),
	FOREIGN KEY (date_key) REFERENCES t_dim_date (date_key),
	FOREIGN KEY (time_key) REFERENCES t_dim_time (time_key),
	FOREIGN KEY (road_key) REFERENCES t_dim_road (road_key),
	FOREIGN KEY (road_event_key) REFERENCES t_dim_road_event (road_event_key)
	c_location POINT NOT NULL,
	heading INT NOT NULL
);

CREATE TABLE t_fact_road
(
	road_key SERIAL PRIMARY KEY,
	vehicle_key INT NOT NULL,
	road_sign_key VARCHAR(10) NOT NULL,
	road_key VARCHAR(10) NOT NULL,
	FOREIGN KEY (vehicle_key) REFERENCES t_dim_vehicle (vehicle_key),
	FOREIGN KEY (road_sign_key) REFERENCES t_dim_road_sign (road_sign_key),
	FOREIGN KEY (road_key) REFERENCES t_dim_road (road_key)
);