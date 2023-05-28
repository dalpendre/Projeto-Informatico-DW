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

#cam_data_path = "../DW/datasets/CAM_data.csv"
#denm_data_path = "../DW/datasets/DENM_data.csv"

#convert binary to decimal
def binary_to_decimal(binary_string):
    return int(binary_string, 2)

#extract data from the tables in the source database
def table_extract(table_name):
    conn = None
    cursor = None
    source_data = None

    try:
        conn = pg.connect(
            database=constants.source_db_name,
            user=constants.db_user,
            password=constants.db_pass,
            host=constants.db_ip_address,
            port=constants.postgres_port
        )
        # print("Connection to PostgreSQL database is successful")
        cursor = conn.cursor()

        #extract data from the source table
        query = "SELECT * FROM " + table_name
        cursor.execute(query)

        source_data = cursor.fetchall()
        for row in source_data:
            print(row)

        print(colors.bcolors.OKGREEN + "Data from table " + table_name + " extracted successfully!\n" + colors.bcolors.ENDC)

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

def extract_cam_data():
    print(colors.bcolors.HEADER + "Extracting CAM data from source database..." + colors.bcolors.ENDC)
    cam_data = table_extract("t_cam")

    #set of rows from the source table to be inserted into the data table
    cam_values = set()

    #convert table values to correspondent dw table values
    for row in cam_data:
        cam_key = row[0]
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
        acceleration_control = row[14]
        stationary_since = row[15]

        #convert latitude, longitude to correct meaurement units
        factor = 0.0000001
        latitude = latitude * factor
        longitude = longitude * factor

        #convert altitude and heading to correct measurement unit
        factor = 0.01
        altitude = altitude * factor
        heading = heading * factor

        #print(latitude)
        #print(longitude)
        #print(altitude)
        #print(heading)

        #convert station type from int to string
        if station_type == 0:
            station_type = "unknown"
        elif station_type == 1:
            station_type = "pedestrian"
        elif station_type == 2:
            station_type = "cyclist"
        elif station_type == 3:
            station_type = "moped"
        elif station_type == 4:
            station_type = "motorcycle"
        elif station_type == 5:
            station_type = "passengerCar"
        elif station_type == 6:
            station_type = "bus"
        elif station_type == 7:
            station_type = "lightTruck"
        elif station_type == 8:
            station_type = "heavyTruck"
        elif station_type == 9:
            station_type = "trailer"
        elif station_type == 10:
            station_type = "specialVehicles"
        elif station_type == 11:
            station_type = "tram"
        elif station_type == 15:
            station_type = "roadSideUnit"

        #convert vehicle role from int to string
        if vehicle_role == 0:
            vehicle_role = "default"
        elif vehicle_role == 1:
            vehicle_role = "publicTransport"
        elif vehicle_role == 2:
            vehicle_role = "specialTransport"
        elif vehicle_role == 3:
            vehicle_role = "dangerousGoods"
        elif vehicle_role == 4:
            vehicle_role = "roadWork"
        elif vehicle_role == 5:
            vehicle_role = "rescue"
        elif vehicle_role == 6:
            vehicle_role = "emergency"
        elif vehicle_role == 7:
            vehicle_role = "safetyCar"
        elif vehicle_role == 8:
            vehicle_role = "agriculture"
        elif vehicle_role == 9:
            vehicle_role = "commercial"
        elif vehicle_role == 10:
            vehicle_role = "military"
        elif vehicle_role == 11:
            vehicle_role = "roadOperator"
        elif vehicle_role == 12:
            vehicle_role = "taxi"
        elif vehicle_role == 13:
            vehicle_role = "reserved1"
        elif vehicle_role == 14:
            vehicle_role = "reserved2"
        elif vehicle_role == 15:
            vehicle_role = "reserved3"

        type_of_fuel = binary_to_decimal(type_of_fuel)
        acceleration_control = binary_to_decimal(acceleration_control)

        if type_of_fuel == 0:
            type_of_fuel = "unknown"
        elif type_of_fuel == 1:
            type_of_fuel = "eletricEnergyStorage"
        elif type_of_fuel == 2:
            type_of_fuel = "liquidPropaneGas"
        elif type_of_fuel == 3:
            type_of_fuel = "compressedNaturalGas"
        elif type_of_fuel == 4:
            type_of_fuel = "diesel"
        elif type_of_fuel == 5:
            type_of_fuel = "gasoline"
        elif type_of_fuel == 6:
            type_of_fuel = "ammonia"

        brakePedalEngaged = False
        gasPedalEngaged = False
        emergencyBrakeEngaged = False
        collisionWarningEngaged = False
        accEngaged = False
        cruiseControlEngaged = False
        speedLimiterEngaged = False

        #convert acceleration control from bitstring to string
        if acceleration_control == 0:
            brakePedalEngaged = True
        elif acceleration_control == 1:
            gasPedalEngaged = True
        elif acceleration_control == 2:
            emergencyBrakeEngaged = True
        elif acceleration_control == 3:
            collisionWarningEngaged = True
        elif acceleration_control == 4:
            accEngaged = True
        elif acceleration_control == 5:
            cruiseControlEngaged = True
        elif acceleration_control == 6:
            speedLimiterEngaged = True

        #convert stationary since from int to string
        if stationary_since == 0:
            stationary_since = "lessThan1Minute"
        elif stationary_since == 1:
            stationary_since = "lessThan2Minutes"
        elif stationary_since == 2:
            stationary_since = "lessThan15Minutes"
        elif stationary_since == 3:
            stationary_since = "equalOrGreater15Minutes"

        cam_message = CamMessage(cam_key, time_key, segment_key, station_id, latitude, longitude, altitude, speed, heading, acceleration, station_type, vehicle_role, time_stamp, type_of_fuel, brakePedalEngaged,
        gasPedalEngaged, emergencyBrakeEngaged, collisionWarningEngaged, accEngaged, cruiseControlEngaged, speedLimiterEngaged, stationary_since)

        #create CAM message
        cam_values.add(cam_message)

    insert_into_data_table("t_data_cam", cam_values)

def extract_denm_data():
    print(colors.bcolors.HEADER + "Extracting DENM data from source database..." + colors.bcolors.ENDC)
    denm_data = table_extract("t_denm")

    denm_values = set()

    for row in denm_data:
        denm_key = row[0]
        time_key = row[1]
        road_event_key = row[2]
        time_stamp = row[3]
        latitude = row[4]
        longitude = row[5]
        altitude = row[6]
        cause = row[7]
        traffic_cause = row[8]
        accident_sub_cause = row[9]
        roadworks_sub_cause = row[10]
        human_presence_on_the_road_sub_cause = row[11]
        wrong_way_driving_sub_cause = row[12]
        adverse_weather_condition_extreme_weather_condition_subCause = row[13]
        adverse_weather_condition_adhesion_sub_cause = row[14]
        adverse_weather_condition_visibility_sub_cause = row[15]
        adverse_weather_condition_precipitation_sub_cause = row[16]
        slow_vehicle_sub_cause = row[17]
        stationary_vehicle_sub_cause = row[18]
        human_problem_sub_cause = row[19]
        emergency_vehicle_approaching_sub_cause = row[20]
        hazardous_location_dangerous_curve_sub_cause = row[21]
        hazardous_location_surface_condition_sub_cause = row[22]
        hazardous_location_obstacle_on_the_road_sub_cause = row[23]
        hazardous_location_animal_on_the_road_sub_cause = row[24]
        collision_risk_sub_cause = row[25]
        signal_violation_sub_cause = row[26]
        rescue_and_recovery_work_in_progress_sub_cause = row[27]
        dangerous_end_of_queue_sub_cause = row[28]
        dangerous_situation_sub_cause = row[29]
        vehicle_breakdown_sub_cause = row[30]
        post_crash_sub_cause = row[31]

        denm_message = DenmMessage(denm_key, time_key, road_event_key, time_stamp, latitude, longitude, altitude, cause, traffic_cause, accident_sub_cause, roadworks_sub_cause, human_presence_on_the_road_sub_cause, wrong_way_driving_sub_cause, adverse_weather_condition_extreme_weather_condition_subCause, adverse_weather_condition_adhesion_sub_cause, adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_sub_cause, human_problem_sub_cause, emergency_vehicle_approaching_sub_cause, hazardous_location_dangerous_curve_sub_cause, hazardous_location_surface_condition_sub_cause, hazardous_location_obstacle_on_the_road_sub_cause, hazardous_location_animal_on_the_road_sub_cause, collision_risk_sub_cause, signal_violation_sub_cause, rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause, dangerous_situation_sub_cause, vehicle_breakdown_sub_cause, post_crash_sub_cause)
        denm_values.add(denm_message)

    insert_into_data_table("t_data_denm", denm_values)

def extract_event_data():
    print(colors.bcolors.HEADER + "Extracting EVENT data from source database..." + colors.bcolors.ENDC)
    event_data = table_extract("t_event")

    event_values = set()

    for row in event_data:
        event_key = row[0]
        designation = row[1]
        start_time = row[2]
        end_time = row[3]
        flag_single_day_event = row[4]

        event = Event(event_key, designation, start_time, end_time, flag_single_day_event)
        event_values.add(event)

    insert_into_data_table("t_data_event", event_values)

def extract_ivim_data():
    print(colors.bcolors.HEADER + "Extracting IVIM data from source database..." + colors.bcolors.ENDC)
    ivim_data = table_extract("t_ivim")

    ivim_values = set()
    for row in ivim_data:
        ivim_key = row[0]
        road_sign_key = row[1]
        zone_key = row[2]
        latitude = row[3]
        longitude = row[4]
        altitude = row[5]

        factor = 0.0000001
        latitude = latitude * factor
        longitude = longitude * factor

        # convert altitude and heading to correct measurement unit
        factor = 0.01
        altitude = altitude * factor

        ivim = IvimMessage(ivim_key, road_sign_key, zone_key, latitude, longitude, altitude)
        ivim_values.add(ivim)

    insert_into_data_table("t_data_ivim", ivim_values)

def extract_road_data():
    print(colors.bcolors.HEADER + "Extracting ROAD data from source database..." + colors.bcolors.ENDC)
    road_data = table_extract("t_road")

    road_values = set()

    for row in road_data:
        road_key = row[0]
        road_name = row[1]
        road_type = row[2]
        road_length = row[3]
        number_of_lanes = row[4]
        start_point = row[5]
        end_point = row[6]

        road = Road(road_key, road_name, road_type, road_length, number_of_lanes, start_point, end_point)
        road_values.add(road)

    insert_into_data_table("t_data_road", road_values)

def extract_road_event_data():
    print(colors.bcolors.HEADER + "Extracting ROAD EVENT data from source database..." + colors.bcolors.ENDC)
    road_event_data = table_extract("t_road_event")

    road_event_values = set()

    #convert table values to correspondent dw table values
    for row in road_event_data:
        road_event_key = row[0]
        description = row[1]
        severity = row[2]
        status = row[3]
        impact_level = row[4]

        road_event = RoadEvent(road_event_key, description, severity, status, impact_level)
        road_event_values.add(road_event)

    insert_into_data_table("t_data_road_event", road_event_values)

def extract_road_sign_data():
    print(colors.bcolors.HEADER + "Extracting ROAD SIGN data from source database..." + colors.bcolors.ENDC)
    road_sign_data = table_extract("t_road_sign")

    road_sign_values = set()

    for row in road_sign_data:
        road_sign_key = row[0]
        road_sign_description = row[1]
        road_sign_code = row[2]
        road_sign_symbol = row[3]
        road_sign_class = row[4]
        road_sign_visibility = row[5]

        road_sign = RoadSign(road_sign_key, road_sign_description, road_sign_code, road_sign_symbol, road_sign_class, road_sign_visibility)
        road_sign_values.add(road_sign)

    insert_into_data_table("t_data_road_sign", road_sign_values)

def extract_segment_data():
    print(colors.bcolors.HEADER + "Extracting SEGMENT data from source database..." + colors.bcolors.ENDC)
    segment_data = table_extract("t_segment")

    segment_values = set()

    for row in segment_data:
        segment_key = row[0]
        road_key = row[1]
        segment_name = row[2]
        segment_type = row[3]
        segment_length = row[4]
        number_of_lanes = row[5]
        start_point = row[6]
        end_point = row[7]

        segment = Segment(segment_key, road_key, segment_name, segment_type, segment_length, number_of_lanes, start_point, end_point)
        segment_values.add(segment)

    insert_into_data_table("t_data_segment", segment_values)

def extract_time_data():
    print(colors.bcolors.HEADER + "Extracting TIME data from source database..." + colors.bcolors.ENDC)
    time_data = table_extract("t_time")

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

        time = Time(time_key, event_key, c_day, c_month, c_year, weekend_day, week_day_number, week_day_name, is_holiday,
                         trimester, semester, season, full_date_description)
        time_values.add(time)

    insert_into_data_table("t_data_time", time_values)

def extract_zone_data():
    print(colors.bcolors.HEADER + "Extracting ZONE data from source database..." + colors.bcolors.ENDC)
    zone_data = table_extract("t_zone")

    zone_values = set()
    for row in zone_data:
        zone_key = row[0]
        zone_name = row[1]
        zone_type = row[2]
        zone_description = row[3]
        zone_area = row[4]

        zone = Zone(zone_key, zone_name, zone_type, zone_description, zone_area)
        zone_values.add(zone)

    insert_into_data_table("t_data_zone", zone_values)

def insert_into_data_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.db_user,
            password=constants.db_pass,
            host=constants.db_ip_address,
            port=constants.postgres_port
        )
        cursor = conn.cursor()

        #insert data into table
        # Execute the query for each set of values
        for row in data:
            # Extract object properties dynamically
            properties = inspect.getmembers(row, lambda x: not (inspect.isroutine(x)))
            property_values = [value for name, value in properties if
                               not name.startswith('__') and not name.endswith('__')]
            column_names = [name for name, _ in properties if not name.startswith('__') and not name.endswith('__')]

            # Construct the SQL query dynamically based on property count
            placeholders = ','.join(['%s'] * len(property_values))
            column_list = ','.join(column_names)
            query = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

            # Execute the query with object property values
            cursor.execute(query, property_values)

        # Commit the changes to the database
        conn.commit()

    except pg.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def truncate_data_tables():
    # Connect to the PostgreSQL database
    conn = pg.connect(
        database=constants.dsa_db_name,
        user=constants.db_user,
        password=constants.db_pass,
        host=constants.db_ip_address,
        port=constants.postgres_port
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Retrieve a list of table names starting with "t_data_"
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name LIKE 't_data_%'")
        table_names = cursor.fetchall()

        # Truncate each table with CASCADE option
        for table_name in table_names:
            cursor.execute(f"TRUNCATE TABLE {table_name[0]} CASCADE")

        # Commit the changes
        conn.commit()
        print("Tables truncated successfully.")

    except pg.Error as e:
        print("Error: Could not truncate tables.")
        print(e)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

truncate_data_tables()

extract_road_event_data()
extract_road_sign_data()
extract_event_data()
extract_time_data()
extract_zone_data()
extract_road_data()
extract_segment_data()
extract_cam_data()
extract_denm_data()
extract_ivim_data()