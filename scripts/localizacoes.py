import pandas as pd
import requests
import sqlalchemy as sql
from sqlalchemy import create_engine
import pyodbc
import urllib.parse

# df = pd.read_csv('C:/Users/Willian/Desktop/Radartona/Radartona2019/Radartona2019/03) SMT_Autuações/INFRACOES_Fev2018.csv', encoding = "latin")

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=mileniobus.cr0kxtgwnksa.us-east-1.rds.amazonaws.com;'
#                       'Database=radartona;'
#                       'UID=milenio;'
#                       'PWD=D12A92B048;')

# df = pd.read_sql("SELECT DISTINCT DescriçãoLocal FROM INFRACOES_Fev2018", conn)

df = pd.read_csv("C:/Users/Willian/Desktop/Radartona/scripts/vdd.csv", sep=";")

for index, row in df.iterrows():
    if index % 500 == 0:
        df.to_csv("C:/Users/Willian/Desktop/Radartona/scripts/teste{}.csv".format(index), sep=";", index=False)
    try:
        rua = row['DescriçãoLocal']
        rua = urllib.parse.quote(rua)
        url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?access_token=pk.eyJ1Ijoid2lsbGlhbmNoYW4iLCJhIjoiY2p5bmgxMW1oMGxkdjNtbzg5NGJ0ZG9lZSJ9.7q1QRjSUZ6L9ehsN1LjnTQ'.format(rua)
        r = requests.get(url)
        print("index: {}".format(index))
        if r.status_code == 200:
            cords = r.json()["features"][0]["center"]
            lat, lon = cords[0], cords[1]
            df.loc[index, 'lat'] = lat
            df.loc[index, 'lon'] = lon
        else:
            df.loc[index, 'lon'] = ""
    except:
        pass

df.to_csv("C:/Users/Willian/Desktop/Radartona/scripts/teste.csv", sep=";", index=False)

# result = pd.merge(org, vdd, left_on="DescriçãoLocal", right_on="DescriçãoLocal", how="left")