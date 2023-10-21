import geopy
import pandas as pd


def load_pto_tur2_data():
    pto_tur2 = pd.read_csv("ptoreal.csv", encoding='iso-8859-1')

def preprocess_pto_tur2():
    pto_tur2 = pd.read_csv("ptoreal.csv", encoding='iso-8859-1')
    pto_tur2 = pto_tur2.drop('HorÃ¡rio Funcionamento', axis=1)
    pto_tur2[['Latitude', 'Longitude']] = pto_tur2['Latitude/Longitude'].str.split(',', expand=True)
    pto_tur2 = pto_tur2.drop('Latitude/Longitude', axis=1)
    pto_tur2['Latitude'] = pto_tur2['Latitude'].str.rstrip(',')

def pto_tur2_histogram_avaliacoes():
    pto_tur2 = pd.read_csv("ptoreal.csv", encoding='iso-8859-1')
    x = pto_tur2['avaliacao'].hist(bins = 10)
    return x

def calcular_distancia (longitude1, latitude1, longitude2, latitude2):
    
    coords_1 = (longitude1, latitude1)
    coords_2 = (longitude2, latitude2)
    
    dist = geopy.distance.geodesic(coords_1, coords_2).km
    return dist
