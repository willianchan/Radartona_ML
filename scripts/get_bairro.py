import pandas as pd
import requests
import sqlalchemy as sql
from sqlalchemy import create_engine
import pyodbc
import urllib.parse

# df = pd.read_csv('C:/Users/Willian/Desktop/Radartona/base_radares.csv')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=mileniobus.cr0kxtgwnksa.us-east-1.rds.amazonaws.com;'
                      'Database=radartona;'
                      'UID=milenio;'
                      'PWD=D12A92B048;')

df = pd.read_sql("SELECT * FROM base_radares", conn)

# df = pd.read_csv("C:/Users/Willian/Desktop/Radartona/scripts/vdd.csv", sep=";")

for index, row in df.iterrows():
    try:
        lat = row['lat']
        lat = urllib.parse.quote(lat)

        lon = row['lon'].replace(";;;;;","")
        lon = urllib.parse.quote(lon)

        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyAaNhuC6LqbfzgmuR8IjwWWUo6OHnhN8aM".format(lat, lon)
        r = requests.get(url)
        print("index: {}".format(index))
        if r.status_code == 200:
            resposta = r.json()
            endereco_comp = resposta["results"][0]["address_components"]

            for end in endereco_comp:
                if "sublocality" in end["types"]:
                    bairro = end['long_name']
                    df.loc[index, 'bairro'] = bairro

    except:
        pass

df.to_csv("C:/Users/Willian/Desktop/Radartona/scripts/bairros.csv", sep=";", index=False)
# url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=-23.50684404,-46.64660688&key=AIzaSyAaNhuC6LqbfzgmuR8IjwWWUo6OHnhN8aM"
# r = requests.get(url)

# resposta = r.json()
# endereco_comp = resposta["results"][0]["address_components"]

# for end in endereco_comp:
#     if "sublocality" in end["types"]:
#         bairro = end['long_name']

# print(resposta)
# result = pd.merge(org, vdd, left_on="DescriçãoLocal", right_on="DescriçãoLocal", how="left")