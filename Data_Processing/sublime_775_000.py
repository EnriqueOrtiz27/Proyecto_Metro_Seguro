from progressbar import *       
import pandas as pd
import numpy as np

widgets = ['Test: ', Percentage(), ' ', Bar(marker='0',left='[',right=']'),
           ' ', ETA(), ' ', FileTransferSpeed()] 

pbar = ProgressBar(widgets=widgets, maxval=500)
pbar.start()


delitos = pd.read_csv('delitos_limpio_v1.csv')
metro = pd.read_csv('estaciones_limpias_v1.csv')

delitos = delitos.drop(columns=['Unnamed: 0', 'index'])
metro = metro.drop(columns=['Unnamed: 0'])

def haversine(lat1, lon1, lat2, lon2):
    import math

    R = 6371000  # radio de la Tierra en metros
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers

    meters = round(meters, 5)
    km = round(km, 3)


    #print(f"Distance: {meters} m")
    return meters


latitudes_metro = list(metro.stop_lat)
longitudes_metro = list(metro.stop_lon)

#El algoritmo funciona. Es tiempo de hacerlo con la base de datos original. 
df_estaciones_crimen = pd.DataFrame(columns=['nombre_estacion', 'stop_lat', 'stop_lon', 
                                             'primera_estacion', 'segunda_estacion', 'tercera_estacion',
                                             'cuarta_estacion'])

for i in range(775000):    
    lst = []
    lat_delito = delitos.iloc[i, 9]
    long_delito = delitos.iloc[i, 8]

    for i in range(len(latitudes_metro)):
        lat_metro = latitudes_metro[i]
        long_metro = longitudes_metro[i]
        pbar.update(i)
        z = haversine(lat_metro, long_metro, lat_delito, long_delito)
        lst.append(z)
        
    minx = min(lst)
    estacion_cerca = pd.DataFrame([metro.iloc[lst.index(minx), :]])
    df_estaciones_crimen = pd.concat([df_estaciones_crimen, estacion_cerca])    

pbar.finish()
print      


estaciones_por_crimen = df_estaciones_crimen.to_csv('sublime_775_000.csv')

print(df_estaciones_crimen.shape)
print(df_estaciones_crimen.head())