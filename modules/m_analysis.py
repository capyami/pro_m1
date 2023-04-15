
import pandas as pd
import numpy as np
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas

def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(lat_start, long_start, lat_finish, long_finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)







def calculate_distances(df_place, df_station):
    distance_of_alls = []
    for index, row in df_place.iterrows():
        distance_one_station = []
        distance_of_alls.append(distance_one_station)
        for index, j in df_station.iterrows():
            distance_one_station.append(distance_meters(float(row['latitude']), float(row['longitude']), float(j['latitude']), float(j['longitude'])))
    df_coordinates = pd.DataFrame(distance_of_alls)
    return df_coordinates



def min_stations(coor, df_bicimad):
    list_min_station_names = {}
    count = 0
    for index, row1 in coor.iterrows():
        for index, row2 in df_bicimad.iterrows():
            if row1['index_station'] == row2['index']:
                list_min_station_names[count]= (row2['name'], row2['address'])
                count = count +1
    df_min_station_names = pd.DataFrame(list_min_station_names)
    df_min_station_names = df_min_station_names.transpose()
    df_min_station_names1 = df_min_station_names.rename(columns={0: "name", 1:'address_station'})
    df_min_station_names_split = df_min_station_names1['name'].apply(lambda x: pd.Series(str(x).split('-')))
    df_min_station_names2 = df_min_station_names_split.rename(columns={0: "numberof", 1:'name_stn', 2:'null'})
    df_min_station_names = pd.concat([df_min_station_names2, df_min_station_names1], axis = 1)
    return df_min_station_names