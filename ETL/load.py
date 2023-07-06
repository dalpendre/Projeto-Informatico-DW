import psycopg2

import colors
import constants

def load_data(source_table, destination_table):
    # Establish connections to both databases
    source_conn = psycopg2.connect(
            database=constants.dsa_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

    destination_conn = psycopg2.connect(
            database=constants.dw_db_name,
            user=constants.username,
            password=constants.password,
            host=constants.host,
            port=constants.port
        )

    # Create cursors for both connections
    source_cursor = source_conn.cursor()
    destination_cursor = destination_conn.cursor()

    try:
        # Retrieve data from the source table
        source_query = f"SELECT * FROM {source_table}"
        source_cursor.execute(source_query)
        data = source_cursor.fetchall()

        # Insert data into the destination table
        destination_query = f"INSERT INTO {destination_table} VALUES ({', '.join(['%s'] * len(data[0]))})"
        destination_cursor.executemany(destination_query, data)

        # Commit the changes to the destination database
        destination_conn.commit()
        print(source_table + ": Data copied successfully!")
    except (psycopg2.Error, psycopg2.DatabaseError) as e:
        print(f"Error: {e}")
        destination_conn.rollback()

    finally:
        # Close the cursors and connections
        source_cursor.close()
        destination_cursor.close()
        source_conn.close()
        destination_conn.close()

print(colors.bcolors.HEADER + "LOAD " + colors.bcolors.ENDC)

load_data("t_clean_road_event", "t_dim_road_event")
load_data("t_clean_road_sign", "t_dim_road_sign")
load_data("t_clean_event", "t_dim_event")
load_data("t_clean_time", "t_dim_time")
load_data("t_clean_zone", "t_dim_zone")
load_data("t_clean_road", "t_dim_road")
load_data("t_clean_segment", "t_dim_segment")
load_data("t_clean_cam", "t_fact_cam")
load_data("t_clean_denm", "t_fact_denm")
load_data("t_clean_ivim", "t_fact_ivim")