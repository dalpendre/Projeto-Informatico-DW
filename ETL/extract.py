import pandas as pd
import psycopg2 as pg
import constants
from classes import Cam, Denm, RoadEvent
from classes.Cam import CamMessage
from classes.Denm import DenmMessage

cam_data_path = "../DW/datasets/CAM_data.csv"
denm_data_path = "../DW/datasets/DENM_data.csv"

#extract data from the tables in the source database
def table_extract(table_name):
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

        # Fetch all rows from the source table
        query = "SELECT * FROM " + table_name
        cursor.execute(query)

        source_data = cursor.fetchall()
        for row in source_data:
            print(row)

    except pg.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

#extract data from a source excel/csv file
def file_extract(path):
    data = pd.read_csv(path)
    return data

def extract_cam_data():
    cam_data = file_extract(cam_data_path)
    insert_into_cam_data_table(cam_data)

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
    file_extract(denm_data_path)

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
    pass

def insert_into_event_data_table():
    pass

def extract_road_data():
    pass

def insert_into_road_data_table():
    pass

def extract_road_event_data():
    pass

def insert_into_road_event_data_table():
    pass

def extract_segment_data():
    pass

def insert_into_segment_data_table():
    pass

extract_cam_data()
extract_denm_data()