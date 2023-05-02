import extract
from classes import Cam, Denm, Ivim, Time, RoadSign, RoadEvent
import psycopg2 as pg

cam_data_path = "../DW/datasets/Viagens/17 Apr/Pombal Leiria/pombal-leiria-17-04-2023-14-26-28.csv"
denm_data_path = "../DW/datasets/Viagens/17 Apr/Pombal Leiria/pombal-leiria-17-04-2023-14-26-28.csv"

def extract_cam_data():
    cam_data = extract.file_extract(cam_data_path)
    insert_into_cam_ext_table(cam_data)

def insert_into_cam_ext_table(cam_data):
    conn = pg.connect(
        database="your_database",
        user="postgres",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()
def extract_denm_data():
    extract.file_extract(denm_data_path)