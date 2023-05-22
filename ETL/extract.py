from time import sleep

import pandas as pd
import psycopg2 as pg
import colors
import constants
from classes import Cam, Denm, Event, Road, RoadEvent, Segment
from classes.Cam import CamMessage
from classes.Denm import DenmMessage

#cam_data_path = "../DW/datasets/CAM_data.csv"
#denm_data_path = "../DW/datasets/DENM_data.csv"

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

        # Fetch all rows from the source table
        query = "SELECT * FROM " + table_name
        cursor.execute(query)

        source_data = cursor.fetchall()
        for row in source_data:
            print(row)

        print(colors.bcolors.OKGREEN + "Data from table " + table_name + " extracted successfully!" + colors.bcolors.ENDC)

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

    #convert table values to correspondent dw table values
    for row in cam_data:
        pass

    #insert_into_cam_data_table(cam_data)

def insert_into_cam_data_table(cam_data):
    try:
        conn = pg.connect(
            database=constants.db_name,
            user=constants.db_user,
            password=constants.db_pass,
            host=constants.db_ip_address,
            port=constants.postgres_port
        )
        print("Connection to PostgreSQL database is successful")
        cursor = conn.cursor()

        #iterate csv file rows and insert into t_ext_cam table
        for index, row in cam_data.iterrows():
            cam_message = CamMessage(row[0], row[1], row[2])
            query = "INSERT INTO t_ext_cam VALUES (%s, %s, %s)"
            cursor.execute(query, (cam_message.cam_key, cam_message.time_key, cam_message.speed))
            conn.commit()
        # Fetch all rows from the table
        query = "SELECT * FROM t_ext_cam"
        cursor.execute(query)

        #print inserted rows on t_ext_cam table
        print("Data  inserted on t_ext_cam table: ")
        db_ext_cam_data = cursor.fetchall()
        for row in db_ext_cam_data:
            print(row)

    except pg.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def extract_denm_data():
    denm_data = table_extract("t_denm")

    #convert table values to correspondent dw table values
    for row in denm_data:
        print(row)

def insert_into_denm_data_table(denm_data):
    try:
        conn = pg.connect(
            database=constants.db_name,
            user=constants.db_user,
            password=constants.db_pass,
            host=constants.db_ip_address,
            port=constants.postgres_port
        )
        print("Connection to PostgreSQL database is successful")
        cursor = conn.cursor()

        #iterate csv file rows and insert into t_ext_cam table
        for index, row in denm_data.iterrows():
            denm_message = DenmMessage(row[0], row[1], row[2], row[3])
            query = "INSERT INTO t_ext_cam VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (denm_message.cam_key, denm_message.time_key, denm_message.c_location, denm_message.speed))
            conn.commit()
        # Fetch all rows from the table
        query = "SELECT * FROM t_ext_denm"
        cursor.execute(query)

        #print inserted rows on t_ext_cam table
        print("Data  inserted on t_ext_cam table: ")
        db_ext_cam_data = cursor.fetchall()
        for row in db_ext_cam_data:
            print(row)

    except pg.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def extract_event_data():
    print(colors.bcolors.HEADER + "Extracting EVENT data from source database..." + colors.bcolors.ENDC)
    event_data = table_extract("t_event")

    #convert table values to correspondent dw table values
    for row in event_data:
        pass

def insert_into_event_data_table():
    pass

def extract_road_data():
    print(colors.bcolors.HEADER + "Extracting ROAD data from source database..." + colors.bcolors.ENDC)
    road_data = table_extract("t_road")

    #convert table values to correspondent dw table values
    for row in road_data:
        pass

def insert_into_road_data_table():
    pass

def extract_road_event_data():
    print(colors.bcolors.HEADER + "Extracting ROAD EVENT data from source database..." + colors.bcolors.ENDC)
    road_event_data = table_extract("t_road_event")

    #convert table values to correspondent dw table values
    for row in road_event_data:
        pass

def insert_into_road_event_data_table():
    pass

def extract_segment_data():
    print(colors.bcolors.HEADER + "Extracting SEGMENT data from source database..." + colors.bcolors.ENDC)
    segment_data = table_extract("t_segment")

    #convert table values to correspondent dw table values
    for row in segment_data:
        pass

def insert_into_segment_data_table():
    pass

def extract_time_data():
    print(colors.bcolors.HEADER + "Extracting TIME data from source database..." + colors.bcolors.ENDC)
    time_data = table_extract("t_time")

    #convert table values to correspondent dw table values
    for row in time_data:
        pass

def insert_into_time_data_table():
    pass

def extract_ivim_data():
    print(colors.bcolors.HEADER + "Extracting IVIM data from source database..." + colors.bcolors.ENDC)
    ivim_data = table_extract("t_ivim")

    #convert table values to correspondent dw table values
    for row in ivim_data:
        pass

def insert_into_ivim_data_table():
    pass

def extract_zone_data():
    print(colors.bcolors.HEADER + "Extracting ZONE data from source database..." + colors.bcolors.ENDC)
    zone_data = table_extract("t_zone")

    #convert table values to correspondent dw table values
    for row in zone_data:
        pass

def insert_into_zone_data_table():
    pass

def extract_road_sign_data():
    print(colors.bcolors.HEADER + "Extracting ROAD SIGN data from source database..." + colors.bcolors.ENDC)
    road_sign_data = table_extract("t_road_sign")

    #convert table values to correspondent dw table values
    for row in road_sign_data:
        pass

def insert_into_road_sign_data_table():
    pass

extract_cam_data()
extract_event_data()
extract_road_data()
extract_road_event_data()
extract_segment_data()
extract_denm_data()
extract_time_data()
extract_ivim_data()
extract_zone_data()
extract_road_sign_data()