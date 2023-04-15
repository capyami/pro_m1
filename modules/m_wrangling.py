
import pandas as pd
import numpy as np
import re





def wrangling_garden(result_api):
    result_select = result_api['@graph']
    df_garden = pd.DataFrame(result_select)
    df_garden_location = df_garden["location"].apply(pd.Series)
    df_garden_address = df_garden["address"].apply(pd.Series)
    df_garden_type = df_garden["@type"].str.replace('https://datos.madrid.es/egob/kos/entidadesYorganismos/', '').fillna("ParquesJardines")
    alls_df_garden = pd.concat([df_garden[['title']], df_garden_location, df_garden_address, df_garden_type], axis = 1)
    df_final_garden = alls_df_garden[['title', '@type', 'locality', 'postal-code', 'street-address', 'latitude', 'longitude']]
    df_final_garden.loc[:, '@type'] = 'Parques Jardines'
    return df_final_garden



def wrangling_bicimad(df_bicimad):
    df_bicimad[['longitude', 'latitude']] = df_bicimad["geometry.coordinates"].apply(lambda x: pd.Series(str(x).replace('[','').replace(']','').split(",")))
    df_bicimad['index'] = df_bicimad.index
    df_bicimad = df_bicimad[['name', 'address', 'latitude', 'longitude','index']]
    return df_bicimad
    



def remove_non_numeric(s):
    return re.sub('[^0-9\.]+', '', s)




def wrangcoor(coor):
    coor = coor.astype(str)
    coor = coor.applymap(lambda x: remove_non_numeric(x))
    coor = coor.astype(float)
    coorm = coor.min(axis=1)
    coorm = coorm.to_dict()
    coor = coor.to_dict()
    dict_ms = {}
    for keys1, values1 in coor.items():
        for key_a, value_a in values1.items():
            for key_min, value_min in coorm.items():
                if value_a == value_min:
                    dict_ms[key_min] = (value_min, keys1)
    coor = dict(sorted(dict_ms.items()))        
    coor = pd.DataFrame.from_dict(coor, orient='index')        
    coor = coor.rename(columns={1: "index_station"})     
    return coor