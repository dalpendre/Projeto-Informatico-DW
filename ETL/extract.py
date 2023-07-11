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

#cam_data_path = "../DW/datasets/CAM_data.csv"
#denm_data_path = "../DW/datasets/DENM_data.csv"

#convert binary to decimal
def binary_to_decimal(binary_string):
    return int(binary_string, 2)

#extract data from the tables in the source database
def table_extract(table_name, key_name):
    conn = None
    cursor = None
    source_data = None

    try:
        conn = pg.connect(
            database=constants.source_db_name,
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
            if os.path.exists("num_lines_in_seeder_" + table_name + ".txt"):
                with open("num_lines_in_seeder_" + table_name + ".txt", "w") as file:
                    file.write(f"Number of rows in table {table_name}: {existing_rows}")
        elif os.path.exists("num_lines_in_seeder_" + table_name + ".txt"):
            with open("num_lines_in_seeder_" + table_name + ".txt", "r") as file:
                existing_rows = int(file.read().strip().split(":")[-1])

        print(existing_rows)
        print(num_rows)

        if num_rows > existing_rows:
            with open("num_lines_in_seeder_" + table_name + ".txt", "w") as file:
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
    cam_data = table_extract("t_cam", "cam_key")

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

        cam_message = CamMessage(time_key, segment_key, station_id, latitude, longitude, altitude, speed, heading, acceleration, station_type, vehicle_role, time_stamp, type_of_fuel, brakePedalEngaged,
        gasPedalEngaged, emergencyBrakeEngaged, collisionWarningEngaged, accEngaged, cruiseControlEngaged, speedLimiterEngaged, stationary_since)

        #create CAM message
        cam_values.add(cam_message)

    insert_into_t_data_cam_table("t_data_cam", cam_values)

def extract_denm_data():
    print(colors.bcolors.HEADER + "Extracting DENM data from source database..." + colors.bcolors.ENDC)
    denm_data = table_extract("t_denm", "denm_key")

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

        if cause == 0:
            cause = "reserved"
        elif cause == 1:
            cause = "trafficCondition"
        elif cause == 2:
            cause = "accident"
        elif cause == 3:
            cause = "roadworks"
        elif cause == 5:
            cause = "impassability"
        elif cause == 6:
            cause = "adverseWeatherCondition_Adhesion"
        elif cause == 7:
            cause = "aquaplannning"
        elif cause == 9:
            cause = "hazardousLocation_SurfaceCondition"
        elif cause == 10:
            cause = "hazardousLocation_ObstacleOnTheRoad"
        elif cause == 11:
            cause = "hazardousLocation_AnimalOnTheRoad"
        elif cause == 12:
            cause = "humanPresenceOnTheRoad"
        elif cause == 14:
            cause = "wrongWayDriving"
        elif cause == 15:
            cause = "rescueAndRecoveryWorkInProgress"
        elif cause == 17:
            cause = "adverseWeatherCondition_ExtremeWeatherCondition"
        elif cause == 18:
            cause = "adverseWeatherCondition_Visibility"
        elif cause == 19:
            cause = "adverseWeatherCondition_Precipitation"
        elif cause == 26:
            cause = "slowVehicle"
        elif cause == 27:
            cause = "dangerousEndOfQueue"
        elif cause == 91:
            cause = "vehicleBreakdown"
        elif cause == 92:
            cause = "postCrash"
        elif cause == 93:
            cause = "humanProblem"
        elif cause == 94:
            cause = "stationaryVehicle"
        elif cause == 95:
            cause = "emergencyVehicleApproaching"
        elif cause == 96:
            cause = "hazardousLocation_DangerousCurve"
        elif cause == 97:
            cause = "collisionRisk"
        elif cause == 98:
            cause = "signalViolation"
        elif cause == 99:
            cause = "dangerousSituation"

        if traffic_cause == 0:
            traffic_cause = "unavailable"
        elif traffic_cause == 1:
            traffic_cause = "increasedVolumeOfTraffic"
        elif traffic_cause == 2:
            traffic_cause = "trafficJamSlowlyIncreasing"
        elif traffic_cause == 3:
            traffic_cause = "trafficJamIncreasing"
        elif traffic_cause == 4:
            traffic_cause = "trafficJamStronglyIncreasing"
        elif traffic_cause == 5:
            traffic_cause = "trafficStationary"
        elif traffic_cause == 6:
            traffic_cause = "trafficJamSlightlyDecreasing"
        elif traffic_cause == 7:
            traffic_cause = "trafficJamDecreasing"
        elif traffic_cause == 8:
            traffic_cause = "trafficJamStronglyDecreasing"

        if accident_sub_cause == 0:
            accident_sub_cause = "unavailable"
        elif accident_sub_cause == 1:
            accident_sub_cause = "multiVehicleAccident"
        elif accident_sub_cause == 2:
            accident_sub_cause = "heavyAccident"
        elif accident_sub_cause == 3:
            accident_sub_cause = "accidentInvolvingLorry"
        elif accident_sub_cause == 4:
            accident_sub_cause = "accidentInvolvingBus"
        elif accident_sub_cause == 5:
            accident_sub_cause = "accidentInvolvingHazardousMaterials"
        elif accident_sub_cause == 6:
            accident_sub_cause = "accidentOnOppositeLane"
        elif accident_sub_cause == 7:
            accident_sub_cause = "unsecuredAccident"
        elif accident_sub_cause == 8:
            accident_sub_cause = "assistanceRequested"

        if road_works_sub_cause == 0:
            road_works_sub_cause = "unavailable"
        elif road_works_sub_cause == 1:
            road_works_sub_cause = "majorRoadworks"
        elif road_works_sub_cause == 2:
            road_works_sub_cause = "roadMarkingWork"
        elif road_works_sub_cause == 3:
            road_works_sub_cause = "slowMovingRoadMaintenance"
        elif road_works_sub_cause == 4:
            road_works_sub_cause = "shortTermStationaryRoadworks"
        elif road_works_sub_cause == 5:
            road_works_sub_cause = "streetCleaning"
        elif road_works_sub_cause == 6:
            road_works_sub_cause = "winterService"

        if human_presence_on_the_road_sub_cause == 0:
            human_presence_on_the_road_sub_cause = "unavailable"
        elif human_presence_on_the_road_sub_cause == 1:
            human_presence_on_the_road_sub_cause = "childrenOnRoadway"
        elif human_presence_on_the_road_sub_cause == 2:
            human_presence_on_the_road_sub_cause = "cyclistOnRoadway"
        elif human_presence_on_the_road_sub_cause == 3:
            human_presence_on_the_road_sub_cause = "motorcyclistOnRoadway"

        if wrong_way_driving_sub_cause == 0:
            wrong_way_driving_sub_cause = "unavailable"
        elif wrong_way_driving_sub_cause == 1:
            wrong_way_driving_sub_cause = "wrongLane"
        elif wrong_way_driving_sub_cause == 2:
            wrong_way_driving_sub_cause = "wrongDirection"

        if adverse_weather_condition_extreme_weather_condition_sub_cause == 0:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "unavailable"
        elif adverse_weather_condition_extreme_weather_condition_sub_cause == 1:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "strongWinds"
        elif adverse_weather_condition_extreme_weather_condition_sub_cause == 2:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "damagingHail"
        elif adverse_weather_condition_extreme_weather_condition_sub_cause == 3:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "hurricane"
        elif adverse_weather_condition_extreme_weather_condition_sub_cause == 4:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "thunderstorm"
        elif adverse_weather_condition_extreme_weather_condition_sub_cause == 5:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "tornado"
        elif adverse_weather_condition_extreme_weather_condition_sub_cause == 6:
            adverse_weather_condition_extreme_weather_condition_sub_cause = "blizzard"

        if adverse_weather_condition_adhesion_sub_cause == 0:
            adverse_weather_condition_adhesion_sub_cause = "unavailable"
        elif adverse_weather_condition_adhesion_sub_cause == 1:
            adverse_weather_condition_adhesion_sub_cause = "heavyFrostOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 2:
            adverse_weather_condition_adhesion_sub_cause = "fuelOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 3:
            adverse_weather_condition_adhesion_sub_cause = "mudOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 4:
            adverse_weather_condition_adhesion_sub_cause = "snowOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 5:
            adverse_weather_condition_adhesion_sub_cause = "iceOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 6:
            adverse_weather_condition_adhesion_sub_cause = "blackIceOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 7:
            adverse_weather_condition_adhesion_sub_cause = "oilOnRoad"
        elif adverse_weather_condition_adhesion_sub_cause == 8:
            adverse_weather_condition_adhesion_sub_cause = "looseChippings"
        elif adverse_weather_condition_adhesion_sub_cause == 9:
            adverse_weather_condition_adhesion_sub_cause = "instantBlackIce"
        elif adverse_weather_condition_adhesion_sub_cause == 10:
            adverse_weather_condition_adhesion_sub_cause = "roadsSalted"

        if adverse_weather_condition_visibility_sub_cause == 0:
            adverse_weather_condition_visibility_sub_cause = "unavailable"
        elif adverse_weather_condition_visibility_sub_cause == 1:
            adverse_weather_condition_visibility_sub_cause = "fog"
        elif adverse_weather_condition_visibility_sub_cause == 2:
            adverse_weather_condition_visibility_sub_cause = "smoke"
        elif adverse_weather_condition_visibility_sub_cause == 3:
            adverse_weather_condition_visibility_sub_cause = "heavySnowfall"
        elif adverse_weather_condition_visibility_sub_cause == 4:
            adverse_weather_condition_visibility_sub_cause = "heavyRain"
        elif adverse_weather_condition_visibility_sub_cause == 5:
            adverse_weather_condition_visibility_sub_cause = "heavyHail"
        elif adverse_weather_condition_visibility_sub_cause == 6:
            adverse_weather_condition_visibility_sub_cause = "lowSunGlare"
        elif adverse_weather_condition_visibility_sub_cause == 7:
            adverse_weather_condition_visibility_sub_cause = "sandstorms"
        elif adverse_weather_condition_visibility_sub_cause == 8:
            adverse_weather_condition_visibility_sub_cause = "swarmsOfInsects"

        if adverse_weather_condition_precipitation_sub_cause == 0:
            adverse_weather_condition_precipitation_sub_cause = "unavailable"
        elif adverse_weather_condition_precipitation_sub_cause == 1:
            adverse_weather_condition_precipitation_sub_cause = "heavyRain"
        elif adverse_weather_condition_precipitation_sub_cause == 2:
            adverse_weather_condition_precipitation_sub_cause = "heavySnowfall"
        elif adverse_weather_condition_precipitation_sub_cause == 3:
            adverse_weather_condition_precipitation_sub_cause = "softHail"

        if slow_vehicle_sub_cause == 0:
            slow_vehicle_sub_cause = "unavailable"
        elif slow_vehicle_sub_cause == 1:
            slow_vehicle_sub_cause = "maintenanceVehicle"
        elif slow_vehicle_sub_cause == 2:
            slow_vehicle_sub_cause = "vehiclesSlowingToLookAtAccident"
        elif slow_vehicle_sub_cause == 3:
            slow_vehicle_sub_cause = "abnormalLoad"
        elif slow_vehicle_sub_cause == 4:
            slow_vehicle_sub_cause = "abnormalWideLoad"
        elif slow_vehicle_sub_cause == 5:
            slow_vehicle_sub_cause = "convoy"
        elif slow_vehicle_sub_cause == 6:
            slow_vehicle_sub_cause = "snowplough"
        elif slow_vehicle_sub_cause == 7:
            slow_vehicle_sub_cause = "deicing"
        elif slow_vehicle_sub_cause == 8:
            slow_vehicle_sub_cause = "saltingVehicles"

        if stationary_vehicle_sub_cause == 0:
            stationary_vehicle_sub_cause = "unavailable"
        elif stationary_vehicle_sub_cause == 1:
            stationary_vehicle_sub_cause = "humanProblem"
        elif stationary_vehicle_sub_cause == 2:
            stationary_vehicle_sub_cause = "vehicleBreakdown"
        elif stationary_vehicle_sub_cause == 3:
            stationary_vehicle_sub_cause = "postCrash"
        elif stationary_vehicle_sub_cause == 4:
            stationary_vehicle_sub_cause = "publicTransportStop"
        elif stationary_vehicle_sub_cause == 5:
            stationary_vehicle_sub_cause = "carryingDangerousGoods"

        if human_problem_sub_cause == 0:
            human_problem_sub_cause = "unavailable"
        elif human_problem_sub_cause == 1:
            human_problem_sub_cause = "glycemiaProblem"
        elif human_problem_sub_cause == 2:
            human_problem_sub_cause = "heartProblem"

        if emergency_vehicle_approaching_sub_cause == 0:
            emergency_vehicle_approaching_sub_cause = "unavailable"
        elif emergency_vehicle_approaching_sub_cause == 1:
            emergency_vehicle_approaching_sub_cause = "emergencyVehicleApproaching"
        elif emergency_vehicle_approaching_sub_cause == 2:
            emergency_vehicle_approaching_sub_cause = "prioritizedVehicleApproaching"

        if hazardous_location_dangerous_curve_sub_cause == 0:
            hazardous_location_dangerous_curve_sub_cause = "unavailable"
        elif hazardous_location_dangerous_curve_sub_cause == 1:
            hazardous_location_dangerous_curve_sub_cause = "dangerousLeftTurnCurve"
        elif hazardous_location_dangerous_curve_sub_cause == 2:
            hazardous_location_dangerous_curve_sub_cause = "dangerousRightTurnCurve"
        elif hazardous_location_dangerous_curve_sub_cause == 3:
            hazardous_location_dangerous_curve_sub_cause = "multipleCurvesStartingWithUnknownTurningDirection"
        elif hazardous_location_dangerous_curve_sub_cause == 4:
            hazardous_location_dangerous_curve_sub_cause = "multipleCurvesStartingWithLeftTurn"
        elif hazardous_location_dangerous_curve_sub_cause == 5:
            hazardous_location_dangerous_curve_sub_cause = "multipleCurvesStartingWithRightTurn"

        if hazardous_location_surface_condition_sub_cause == 0:
            hazardous_location_surface_condition_sub_cause = "unavailable"
        elif hazardous_location_surface_condition_sub_cause == 1:
            hazardous_location_surface_condition_sub_cause = "rockfalls"
        elif hazardous_location_surface_condition_sub_cause == 2:
            hazardous_location_surface_condition_sub_cause = "earthquakeDamage"
        elif hazardous_location_surface_condition_sub_cause == 3:
            hazardous_location_surface_condition_sub_cause = "sewerCollapse"
        elif hazardous_location_surface_condition_sub_cause == 4:
            hazardous_location_surface_condition_sub_cause = "subsidence"
        elif hazardous_location_surface_condition_sub_cause == 5:
            hazardous_location_surface_condition_sub_cause = "snowDrifts"
        elif hazardous_location_surface_condition_sub_cause == 6:
            hazardous_location_surface_condition_sub_cause = "stormDamage"
        elif hazardous_location_surface_condition_sub_cause == 7:
            hazardous_location_surface_condition_sub_cause = "burstPipe"
        elif hazardous_location_surface_condition_sub_cause == 8:
            hazardous_location_surface_condition_sub_cause = "volcanoEruption"
        elif hazardous_location_surface_condition_sub_cause == 9:
            hazardous_location_surface_condition_sub_cause = "fallingIce"

        if hazardous_location_obstacle_on_the_road_sub_cause == 0:
            hazardous_location_obstacle_on_the_road_sub_cause = "unavailable"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 1:
            hazardous_location_obstacle_on_the_road_sub_cause = "shedLoad"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 2:
            hazardous_location_obstacle_on_the_road_sub_cause = "partsOfVehicles"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 3:
            hazardous_location_obstacle_on_the_road_sub_cause = "partsOfTyres"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 4:
            hazardous_location_obstacle_on_the_road_sub_cause = "bigObjects"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 5:
            hazardous_location_obstacle_on_the_road_sub_cause = "fallenTrees"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 6:
            hazardous_location_obstacle_on_the_road_sub_cause = "hubCaps"
        elif hazardous_location_obstacle_on_the_road_sub_cause == 7:
            hazardous_location_obstacle_on_the_road_sub_cause = "waitingVehicles"

        if hazardous_location_animal_on_the_road_sub_cause == 0:
            hazardous_location_animal_on_the_road_sub_cause = "unavailable"
        elif hazardous_location_animal_on_the_road_sub_cause == 1:
            hazardous_location_animal_on_the_road_sub_cause = "wildAnimals"
        elif hazardous_location_animal_on_the_road_sub_cause == 2:
            hazardous_location_animal_on_the_road_sub_cause = "herdOfAnimals"
        elif hazardous_location_animal_on_the_road_sub_cause == 3:
            hazardous_location_animal_on_the_road_sub_cause = "smallAnimals"
        elif hazardous_location_animal_on_the_road_sub_cause == 4:
            hazardous_location_animal_on_the_road_sub_cause = "largeAnimals"

        if collision_risk_sub_cause == 0:
            collision_risk_sub_cause = "unavailable"
        elif collision_risk_sub_cause == 1:
            collision_risk_sub_cause = "longitudinalCollisionRisk"
        elif collision_risk_sub_cause == 2:
            collision_risk_sub_cause = "crossingCollisionRisk"
        elif collision_risk_sub_cause == 3:
            collision_risk_sub_cause = "lateralCollisionRisk"
        elif collision_risk_sub_cause == 4:
            collision_risk_sub_cause = "vulnerableRoadUser"

        if signal_violation_sub_cause == 0:
            signal_violation_sub_cause = "unavailable"
        elif signal_violation_sub_cause == 1:
            signal_violation_sub_cause = "stopSignViolation"
        elif signal_violation_sub_cause == 2:
            signal_violation_sub_cause = "trafficLightViolation"
        elif signal_violation_sub_cause == 3:
            signal_violation_sub_cause = "turningRegulationViolation"

        if rescue_and_recovery_work_in_progress_sub_cause == 0:
            rescue_and_recovery_work_in_progress_sub_cause = "unavailable"
        elif rescue_and_recovery_work_in_progress_sub_cause == 1:
            rescue_and_recovery_work_in_progress_sub_cause = "emergencyVehicles"
        elif rescue_and_recovery_work_in_progress_sub_cause == 2:
            rescue_and_recovery_work_in_progress_sub_cause = "rescueHelicopterLanding"
        elif rescue_and_recovery_work_in_progress_sub_cause == 3:
            rescue_and_recovery_work_in_progress_sub_cause = "policeActivityOngoing"
        elif rescue_and_recovery_work_in_progress_sub_cause == 4:
            rescue_and_recovery_work_in_progress_sub_cause = "medicalEmergencyOngoing"
        elif rescue_and_recovery_work_in_progress_sub_cause == 5:
            rescue_and_recovery_work_in_progress_sub_cause = "childAbductionInProgress"

        if dangerous_end_of_queue_sub_cause == 0:
            dangerous_end_of_queue_sub_cause = "unavailable"
        elif dangerous_end_of_queue_sub_cause == 1:
            dangerous_end_of_queue_sub_cause = "suddenEndOfQueue"
        elif dangerous_end_of_queue_sub_cause == 2:
            dangerous_end_of_queue_sub_cause = "queueOverHill"
        elif dangerous_end_of_queue_sub_cause == 3:
            dangerous_end_of_queue_sub_cause = "queueAroundBend"
        elif dangerous_end_of_queue_sub_cause == 4:
            dangerous_end_of_queue_sub_cause = "queueInTunnel"

        if dangerous_situation_sub_cause == 0:
            dangerous_situation_sub_cause = "unavailable"
        elif dangerous_situation_sub_cause == 1:
            dangerous_situation_sub_cause = "emergencyElectronicBrakeEngaged"
        elif dangerous_situation_sub_cause == 2:
            dangerous_situation_sub_cause = "preCrashSystemEngaged"
        elif dangerous_situation_sub_cause == 3:
            dangerous_situation_sub_cause = "espEngaged"
        elif dangerous_situation_sub_cause == 4:
            dangerous_situation_sub_cause = "absEngaged"
        elif dangerous_situation_sub_cause == 5:
            dangerous_situation_sub_cause = "aebEngaged"
        elif dangerous_situation_sub_cause == 6:
            dangerous_situation_sub_cause = "brakeWarningEngaged"
        elif dangerous_situation_sub_cause == 7:
            dangerous_situation_sub_cause = "collisionRiskWarningEngaged"

        if vehicle_break_down_sub_cause == 0:
            vehicle_break_down_sub_cause = "unavailable"
        elif vehicle_break_down_sub_cause == 1:
            vehicle_break_down_sub_cause = "lackOfFuel"
        elif vehicle_break_down_sub_cause == 2:
            vehicle_break_down_sub_cause = "lackOfBatteryPower"
        elif vehicle_break_down_sub_cause == 3:
            vehicle_break_down_sub_cause = "engineProblem"
        elif vehicle_break_down_sub_cause == 4:
            vehicle_break_down_sub_cause = "transmissionProblem"
        elif vehicle_break_down_sub_cause == 5:
            vehicle_break_down_sub_cause = "engineCoolingProblem"
        elif vehicle_break_down_sub_cause == 6:
            vehicle_break_down_sub_cause = "brakingSystemProblem"
        elif vehicle_break_down_sub_cause == 7:
            vehicle_break_down_sub_cause = "steeringProblem"
        elif vehicle_break_down_sub_cause == 8:
            vehicle_break_down_sub_cause = "tyrePuncture"
        elif vehicle_break_down_sub_cause == 9:
            vehicle_break_down_sub_cause = "tyrePressureProblem"

        if post_crash_sub_cause == 0:
            post_crash_sub_cause = "unavailable"
        elif post_crash_sub_cause == 1:
            post_crash_sub_cause = "accidentWithoutECallTriggered"
        elif post_crash_sub_cause == 2:
            post_crash_sub_cause = "accidentWithECallManuallyTriggered"
        elif post_crash_sub_cause == 3:
            post_crash_sub_cause = "accidentWithECallAutomaticallyTriggered"
        elif post_crash_sub_cause == 4:
            post_crash_sub_cause = "accidentWithECallTriggeredWithoutAccessToCellularNetwork"

        factor = 0.0000001
        latitude = latitude * factor
        longitude = longitude * factor

        # convert altitude and heading to correct measurement unit
        factor = 0.01
        altitude = altitude * factor

        denm_message = DenmMessage(time_key, road_event_key, time_stamp, latitude, longitude, altitude, heading, cause, traffic_cause, road_works_sub_cause,
                 accident_sub_cause, slow_vehicle_sub_cause, stationary_vehicle_sub_cause, human_presence_on_the_road_sub_cause,
                 collision_risk_sub_cause, dangerous_situation_sub_cause, vehicle_break_down_sub_cause, post_crash_sub_cause,
                 human_problem_sub_cause, adverse_weather_condition_extreme_weather_condition_sub_cause, adverse_weather_condition_adhesion_sub_cause,
                 adverse_weather_condition_visibility_sub_cause, adverse_weather_condition_precipitation_sub_cause, emergency_vehicle_approaching_sub_cause,
                 hazardous_location_dangerous_curve_sub_cause, hazardous_location_surface_condition_sub_cause, hazardous_location_obstacle_on_the_road_sub_cause,
                 hazardous_location_animal_on_the_road_sub_cause, rescue_and_recovery_work_in_progress_sub_cause, dangerous_end_of_queue_sub_cause,
                 signal_violation_sub_cause, wrong_way_driving_sub_cause)
        denm_values.add(denm_message)
    insert_into_t_data_denm_table("t_data_denm", denm_values)

def extract_event_data():
    print(colors.bcolors.HEADER + "Extracting EVENT data from source database..." + colors.bcolors.ENDC)
    event_data = table_extract("t_event", "event_key")

    event_values = set()

    for row in event_data:
        designation = row[1]
        start_time = row[2]
        end_time = row[3]
        flag_single_day_event = row[4]

        event = Event(designation, start_time, end_time, flag_single_day_event)
        event_values.add(event)

    insert_into_data_table("t_data_event", event_values)

def extract_ivim_data():
    print(colors.bcolors.HEADER + "Extracting IVIM data from source database..." + colors.bcolors.ENDC)
    ivim_data = table_extract("t_ivim", "ivim_key")

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

        ivim = IvimMessage(ivim_key,road_sign_key, zone_key, latitude, longitude, altitude)
        ivim_values.add(ivim)

    insert_into_t_data_ivim_table("t_data_ivim", ivim_values)

def extract_road_data():
    print(colors.bcolors.HEADER + "Extracting ROAD data from source database..." + colors.bcolors.ENDC)
    road_data = table_extract("t_road", "road_key")

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

    insert_into_data_table("t_data_road", road_values)

def extract_road_event_data():
    print(colors.bcolors.HEADER + "Extracting ROAD EVENT data from source database..." + colors.bcolors.ENDC)
    road_event_data = table_extract("t_road_event", "road_event_key")

    road_event_values = set()

    #convert table values to correspondent dw table values
    for row in road_event_data:
        description = row[1]
        severity = row[2]
        status = row[3]
        impact_level = row[4]

        road_event = RoadEvent(description, severity, status, impact_level)
        road_event_values.add(road_event)

    insert_into_data_table("t_data_road_event", road_event_values)

def extract_road_sign_data():
    print(colors.bcolors.HEADER + "Extracting ROAD SIGN data from source database..." + colors.bcolors.ENDC)
    road_sign_data = table_extract("t_road_sign", "road_sign_key")

    road_sign_values = set()

    for row in road_sign_data:
        road_sign_description = row[1]
        road_sign_code = row[2]
        road_sign_symbol = row[3]
        road_sign_class = row[4]
        road_sign_visibility = row[5]

        road_sign = RoadSign(road_sign_description, road_sign_code, road_sign_symbol, road_sign_class, road_sign_visibility)
        road_sign_values.add(road_sign)

    insert_into_data_table("t_data_road_sign", road_sign_values)

def extract_segment_data():
    print(colors.bcolors.HEADER + "Extracting SEGMENT data from source database..." + colors.bcolors.ENDC)
    segment_data = table_extract("t_segment", "segment_key")

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

    insert_into_t_data_segment_table("t_data_segment", segment_values)

def extract_time_data():
    print(colors.bcolors.HEADER + "Extracting TIME data from source database..." + colors.bcolors.ENDC)
    time_data = table_extract("t_time", "time_key")

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

    insert_into_t_data_time_table("t_data_time", time_values)

def extract_zone_data():
    print(colors.bcolors.HEADER + "Extracting ZONE data from source database..." + colors.bcolors.ENDC)
    zone_data = table_extract("t_zone", "zone_key")

    zone_values = set()
    for row in zone_data:
        zone_key = row[0]
        zone_name = row[1]
        zone_type = row[2]
        zone_description = row[3]
        zone_area = row[4]

        zone = Zone(zone_key,zone_name, zone_type, zone_description, zone_area)
        zone_values.add(zone)

    insert_into_data_table("t_data_zone", zone_values)

def insert_into_data_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_data_time_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_data_segment_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_data_cam_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_data_cam_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_into_t_data_denm_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
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
        user=constants.username,
        password=constants.password,
        host=constants.host,
        port=constants.port
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

def insert_into_t_data_ivim_table(table_name, data):
    conn = None
    cursor = None

    try:
        conn = pg.connect(
            database=constants.dsa_db_name,
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
        print("Error: Could not make a connection to the Postgres database (extract)")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#truncate_data_tables()

print(colors.bcolors.HEADER + "EXTRACT " + colors.bcolors.ENDC)

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