import pandas as pd
import  psycopg2 as pg

def file_extract(path):
    data = pd.read_csv(path)
    print(data)
    return data