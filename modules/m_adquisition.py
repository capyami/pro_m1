
import requests
import json
import duckdb
import pandas as pd
import numpy as np


def adquisition_gardens():
    response = requests.get('https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.json')
    results_api = response.json()
    return results_api


def adquisition_db_bicimad():
    db_bicimad = duckdb.connect('./data/bicimad.db')
    df_bicimad = db_bicimad.sql('select * from bicimad_stations').df()
    return df_bicimad