#load from t_data tables and clean incorrect or bad data
import os

import psycopg2 as pg
from psycopg2 import Error

import colors
import constants

def truncate_tables():
    try:
        connection = pg.connect(
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port,
            database=constants.dsa_db_name
        )

        cursor = connection.cursor()

        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name LIKE 't_clean_%'")
        table_names = cursor.fetchall()

        for table_name in table_names:
            cursor.execute(f"TRUNCATE TABLE {table_name[0]} RESTART IDENTITY CASCADE")

        connection.commit()
        print("Tables truncated successfully!")

    except (Exception, Error) as error:
        print("Error while truncating tables:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def transform_road_event_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_road_sign_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_event_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_time_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_zone_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_road_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_segment_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_cam_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_denm_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def transform_ivim_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = pg.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

        # Create a cursor
        cursor = conn.cursor()

        # Copy data from source table to destination table
        query = f"INSERT INTO {destination_table} SELECT * FROM {source_table}"
        cursor.execute(query)

        # Commit the transaction
        conn.commit()

        print(f"Data copied from {source_table} to {destination_table} successfully.")

    except pg.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

print(colors.bcolors.HEADER + "TRANSFORM " + colors.bcolors.ENDC)

truncate_tables()
transform_road_event_data("t_data_road_event", "t_clean_road_event")
transform_road_sign_data("t_data_road_sign", "t_clean_road_sign")
transform_event_data("t_data_event", "t_clean_event")
transform_time_data("t_data_time", "t_clean_time")
transform_zone_data("t_data_zone", "t_clean_zone")
transform_road_data("t_data_road", "t_clean_road")
transform_segment_data("t_data_segment", "t_clean_segment")
transform_cam_data("t_data_cam", "t_clean_cam")
transform_denm_data("t_data_denm", "t_clean_denm")
transform_ivim_data("t_data_ivim", "t_clean_ivim")