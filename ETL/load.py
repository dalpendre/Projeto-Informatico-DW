import os
from time import sleep
import pandas as pd
import psycopg2 as pg
import colors
import constants
import inspect
from classes.Cam import CamMessage
from classes.Denm import DenmMessage
from classes.Event import Event
from classes.Ivim import IvimMessage
from classes.Road import Road
from classes.RoadEvent import RoadEvent
from classes.RoadSign import RoadSign
from classes.Segment import Segment
from classes.Time import Time
from classes.Zone import Zone

#extract data from the tables in the source database
def table_extract(table_name, key_name):
    conn = None
    cursor = None
    source_data = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        # print("Connection to PostgreSQL database is successful")
        cursor = conn.cursor()

        query = "SELECT * FROM " + table_name
        cursor.execute(query)

        #all rows from the table
        source_data = cursor.fetchall()

        existing_rows = 0
        num_rows = len(source_data)

        if num_rows == 0:
            existing_rows = 0
            if os.path.exists("num_lines_in_transform_" + table_name + ".txt"):
                with open("num_lines_in_transform_" + table_name + ".txt", "w") as file:
                    file.write(f"Number of rows in table {table_name}: {existing_rows}")
        elif os.path.exists("num_lines_in_transform_" + table_name + ".txt"):
            with open("num_lines_in_transform_" + table_name + ".txt", "r") as file:
                existing_rows = int(file.read().strip().split(":")[-1])

        print(existing_rows)
        print(num_rows)

        if num_rows > existing_rows:
            with open("num_lines_in_transform_" + table_name + ".txt", "w") as file:
                file.write(f"Number of rows in table {table_name}: {num_rows}")

        # calculate how many new lines were added to the table
        num_new_lines = num_rows - existing_rows

        if num_new_lines <= 0:
            return []

        # extract data from the source table
        query = "SELECT * FROM " + table_name + " ORDER BY " + key_name + " DESC LIMIT " + str(num_new_lines);
        cursor.execute(query)

        #new rows from the table
        source_data = cursor.fetchall()

        for row in source_data:
            print(row)

        print(colors.bcolors.OKGREEN + "Data from table " + table_name + " loaded successfully!\n" + colors.bcolors.ENDC)

    except pg.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return source_data

#extract data from a source excel/csv file
def file_extract(path):
    data = pd.read_csv(path)
    return data

def load_cam_data():
    print(colors.bcolors.HEADER + "Loading CAM data from dsa database..." + colors.bcolors.ENDC)
    cam_data = table_extract("t_clean_cam", "cam_key")

    #set of rows from the source table to be inserted into the data table
    cam_values = set()

    #convert table values to correspondent dw table values
    for row in cam_data:
        time_key = row[1]
        segment_key = row[2]
        station_id = row[3]
        latitude = row[4]
        longitude = row[5]
        altitude = row[6]
        speed = row[7]
        heading = row[8]
        acceleration = row[9]
        station_type = row[10]
        vehicle_role = row[11]
        time_stamp = row[12]
        type_of_fuel = row[13]
        brakePedalEngaged = row[14]
        gasPedalEngaged = row[15]
        emergencyBrakeEngaged = row[16]
        collisionWarningEngaged = row[17]
        accEngaged = row[18]
        cruiseControlEngaged = row[19]
        speedLimiterEngaged = row[20]
        stationary_since = row[21]

        cam_message = CamMessage(time_key, segment_key, station_id, latitude, longitude, altitude, speed, heading, acceleration, station_type, vehicle_role, time_stamp, type_of_fuel, brakePedalEngaged,
        gasPedalEngaged, emergencyBrakeEngaged, collisionWarningEngaged, accEngaged, cruiseControlEngaged, speedLimiterEngaged, stationary_since)

        #create CAM message
        cam_values.add(cam_message)

    insert_into_t_fact_cam_table("t_fact_cam", cam_values)

def load_denm_data():
    print(colors.bcolors.HEADER + "Loading DENM data from source database..." + colors.bcolors.ENDC)
    denm_data = table_extract("t_clean_denm", "denm_key")

    denm_values = set()

    for row in denm_data:
        time_key = row[1]
        road_event_key = row[2]
        time_stamp = row[3]
        latitude = row[4]
        longitude = row[5]
        altitude = row[6]
        heading = row[7]
        cause = row[8]
        traffic_cause = row[9]
        road_works_sub_cause = row[10]
        accident_sub_cause = row[11]
        slow_vehicle_sub_cause = row[12]
        stationary_vehicle_sub_cause = row[13]
        human_problem_sub_cause = row[14]
        collision_risk_sub_cause = row[15]
        human_presence_on_the_road_sub_cause = row[16]
        dangerous_situation_sub_cause = row[17]
        vehicle_break_down_sub_cause = row[18]
        post_crash_sub_cause = row[19]
        adverse_weather_condition_extreme_weather_condition_sub_cause = row[20]
        adverse_weather_condition_adhesion_sub_cause = row[21]
        adverse_weather_condition_visibility_sub_cause = row[22]
        adverse_weather_condition_precipitation_sub_cause = row[23]
        emergency_vehicle_approaching_sub_cause = row[24]
        hazardous_location_dangerous_curve_sub_cause = row[25]
        hazardous_location_surface_condition_sub_cause = row[26]
        hazardous_location_obstacle_on_the_road_sub_cause = row[27]
        hazardous_location_animal_on_the_road_sub_cause = row[28]
        rescue_and_recovery_work_in_progress_sub_cause = row[29]
        dangerous_end_of_queue_sub_cause = row[30]
        signal_violation_sub_cause = row[31]
        wrong_way_driving_sub_cause = row[32]

        denm_message = DenmMessage(time_key, road_event_key, time_stamp, latitude, longitude, altitude, heading, cause, traffic_cause, road_works_sub_cause,
                 accident_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_sub_cause, human_presence_on_the_road_sub_cause,
                 collision_risk_sub_cause, dangerous_situation_sub_cause, vehicle_break_down_sub_cause, post_crash_sub_cause,
                 human_problem_sub_cause, adverse_weather_condition_extreme_weather_condition_sub_cause, adverse_weather_condition_adhesion_sub_cause,
                 adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause, emergency_vehicle_approaching_sub_cause,
                 hazardous_location_dangerous_curve_sub_cause, hazardous_location_surface_condition_sub_cause, hazardous_location_obstacle_on_the_road_sub_cause,
                 hazardous_location_animal_on_the_road_sub_cause, rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause,
                 signal_violation_sub_cause, wrong_way_driving_sub_cause)
        denm_values.add(denm_message)
    insert_into_t_fact_denm_table("t_fact_denm", denm_values)

def load_event_data():
    print(colors.bcolors.HEADER + "Loading EVENT data from dsa database..." + colors.bcolors.ENDC)
    event_data = table_extract("t_clean_event", "event_key")

    event_values = set()

    for row in event_data:
        designation = row[1]
        start_time = row[2]
        end_time = row[3]
        flag_single_day_event = row[4]

        event = Event(designation, start_time, end_time, flag_single_day_event)
        event_values.add(event)

    insert_into_dim_table("t_dim_event", event_values)

def load_ivim_data():
    print(colors.bcolors.HEADER + "Loading IVIM data from dsa database..." + colors.bcolors.ENDC)
    ivim_data = table_extract("t_clean_ivim", "ivim_key")

    ivim_values = set()
    for row in ivim_data:
        ivim_key = row[0]
        road_sign_key = row[1]
        zone_key = row[2]
        latitude = row[3]
        longitude = row[4]
        altitude = row[5]

        ivim = IvimMessage(ivim_key,road_sign_key, zone_key, latitude, longitude, altitude)
        ivim_values.add(ivim)

    insert_into_t_fact_ivim_table("t_fact_ivim", ivim_values)

def load_road_data():
    print(colors.bcolors.HEADER + "Loading ROAD data from dsa database..." + colors.bcolors.ENDC)
    road_data = table_extract("t_clean_road", "road_key")

    road_values = set()

    for row in road_data:
        road_name = row[1]
        road_type = row[2]
        road_length = row[3]
        number_of_lanes = row[4]
        start_point = row[5]
        end_point = row[6]

        road = Road(road_name, road_type, road_length, number_of_lanes, start_point, end_point)
        road_values.add(road)

    insert_into_dim_table("t_dim_road", road_values)

def load_road_event_data():
    print(colors.bcolors.HEADER + "Loading ROAD EVENT data from dsa database..." + colors.bcolors.ENDC)
    road_event_data = table_extract("t_clean_road_event", "road_event_key")

    road_event_values = set()

    #convert table values to correspondent dw table values
    for row in road_event_data:
        description = row[1]
        severity = row[2]
        status = row[3]
        impact_level = row[4]

        road_event = RoadEvent(description, severity, status, impact_level)
        road_event_values.add(road_event)

    insert_into_dim_table("t_dim_road_event", road_event_values)

def load_road_sign_data():
    print(colors.bcolors.HEADER + "Loading ROAD SIGN data from dsa database..." + colors.bcolors.ENDC)
    road_sign_data = table_extract("t_clean_road_sign", "road_sign_key")

    road_sign_values = set()

    for row in road_sign_data:
        road_sign_description = row[1]
        road_sign_code = row[2]
        road_sign_symbol = row[3]
        road_sign_class = row[4]
        road_sign_visibility = row[5]

        road_sign = RoadSign(road_sign_description, road_sign_code, road_sign_symbol, road_sign_class, road_sign_visibility)
        road_sign_values.add(road_sign)

    insert_into_dim_table("t_dim_road_sign", road_sign_values)

def load_segment_data():
    print(colors.bcolors.HEADER + "Loading SEGMENT data from dsa database..." + colors.bcolors.ENDC)
    segment_data = table_extract("t_clean_segment", "segment_key")

    segment_values = set()

    for row in segment_data:
        segment_key = [0]
        road_key = row[1]
        segment_name = row[2]
        segment_type = row[3]
        segment_length = row[4]
        number_of_lanes = row[5]
        start_point = row[6]
        end_point = row[7]

        segment = Segment(segment_key,road_key, segment_name, segment_type, segment_length, number_of_lanes, start_point, end_point)
        segment_values.add(segment)

    insert_into_t_dim_segment_table("t_dim_segment", segment_values)

def load_time_data():
    print(colors.bcolors.HEADER + "Loading TIME data from dsa database..." + colors.bcolors.ENDC)
    time_data = table_extract("t_clean_time", "time_key")

    time_values = set()
    for row in time_data:
        time_key = row[0]
        event_key = row[1]
        c_day = row[2]
        c_month = row[3]
        c_year = row[4]
        weekend_day = row[5]
        week_day_number = row[6]
        week_day_name = row[7]
        is_holiday = row[8]
        trimester = row[9]
        semester = row[10]
        season = row[11]
        full_date_description = row[12]

        time = Time(time_key,event_key, c_day, c_month, c_year, weekend_day, week_day_number, week_day_name, is_holiday, trimester, semester, season, full_date_description)
        time_values.add(time)

    insert_into_t_dim_time_table("t_dim_time", time_values)

def load_zone_data():
    print(colors.bcolors.HEADER + "Loading ZONE data from dsa database..." + colors.bcolors.ENDC)
    zone_data = table_extract("t_data_zone", "zone_key")

    zone_values = set()
    for row in zone_data:
        zone_key = row[0]
        zone_name = row[1]
        zone_type = row[2]
        zone_description = row[3]
        zone_area = row[4]

        zone = Zone(zone_key,zone_name, zone_type, zone_description, zone_area)
        zone_values.add(zone)

    insert_into_dim_table("t_dim_zone", zone_values)

def insert_into_dim_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database (load)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_dim_time_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Include the event_key column
            column_names.append('event_key')
            property_values.append(row.event_key)

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database (load)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_dim_segment_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Include the event_key column
            column_names.append('road_key')
            property_values.append(row.road_key)

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database (load)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_fact_cam_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Include the event_key column
            column_names.append('time_key')
            property_values.append(row.time_key)
            column_names.append('segment_key')
            property_values.append(row.segment_key)

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database (load)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_fact_cam_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Include the event_key column
            column_names.append('time_key')
            property_values.append(row.time_key)
            column_names.append('segment_key')
            property_values.append(row.segment_key)

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database (load)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_fact_denm_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Include the event_key column
            column_names.append('time_key')
            property_values.append(row.time_key)
            column_names.append("road_event_key")
            property_values.append(row.road_event_key)

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database (load)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def truncate_clean_tables():
    # Connect to the PostgreSQL database
    conn = pg.connect(
        database=constants.dsa_db_name,
        user=constants.username,
        password=constants.password,
        host=constants.host,
        port=constants.port
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Retrieve a list of table names starting with "t_data_"
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name LIKE 't_clean_%'")
        table_names = cursor.fetchall()

        # Truncate each table with CASCADE option
        for table_name in table_names:
            cursor.execute(f"TRUNCATE TABLE {table_name[0]} CASCADE")

        # Commit the changes
        conn.commit()
        #print("Tables truncated successfully.")

    except pg.Error as e:
        print("Error: Could not truncate tables.")
        print(e)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def insert_into_t_fact_ivim_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )
        cursor = conn.cursor()

        # Insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically excluding primary key
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]
            column_names = [name for name, _ in properties if
                            not name.startswith('__') and not name.endswith('__') and not name.endswith('_key')]

            # Include the event_key column
            column_names.append('road_sign_key')
            property_values.append(row.road_sign_key)
            column_names.append("zone_key")
            property_values.append(row.zone_key)

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make a connection to the Postgres database ()")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

print(colors.bcolors.HEADER + "LOAD " + colors.bcolors.ENDC)

load_road_event_data()
load_road_sign_data()
load_event_data()
load_time_data()
load_zone_data()
load_road_data()
load_segment_data()
load_cam_data()
load_denm_data()
load_ivim_data()

#truncate_clean_tables()