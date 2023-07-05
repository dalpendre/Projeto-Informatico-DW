#load t_clean tables to the data warehouse tables
import psycopg2

import colors
import constants

def load_road_event_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_road_sign_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_event_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_time_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_zone_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_road_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_segment_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_cam_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_denm_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_ivim_data(source_table, destination_table):
    try:
        # Connect to the database
        conn = psycopg2.connect(
            database=constants.dw_db_name,
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

    except psycopg2.Error as e:
        print("Error: Could not copy data from table.")
        print(e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

print(colors.bcolors.HEADER + "LOAD " + colors.bcolors.ENDC)

load_road_event_data("t_clean_road_event","t_dim_road_event")
load_road_sign_data("t_clean_road_sign","t_dim_road_sign")
load_event_data("t_clean_event","t_dim_event")
load_time_data("t_clean_time","t_dim_time")
load_zone_data("t_clean_zone","t_dim_zone")
load_road_data("t_clean_road","t_dim_road")
load_segment_data("t_clean_segment","t_dim_segment")
load_cam_data("t_clean_cam","t_fact_cam")
load_denm_data("t_clean_denm","t_fact_denm")
load_ivim_data("t_clean_ivim","t_fact_ivim")
