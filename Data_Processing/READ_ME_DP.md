# Data Processing.

En esta sección hay pocos archivos. Pero es importante. Recordemos que ninguna parte del proyecto hubiera funcionado sin una manera de relacionar la base de datos que contiene los delitos con la base de datos de las estaciones de metro. En esta sección logré encontrar tal puente. 

## La fórmula del haversine. 

La forma en que logré esto es usando la fórmula del haversine, que te permite encontrar la distancia entre dos pares de coordenadas geográficas; es decir, dos pares de números en la forma (latitud, longitud). 

Computacionalmente hablando, esta fue la parte más pesada para mi computadora. El archivo 'sublime_775_000.py' tardó más de 8 horas en correr. 

Básicamente funcionó así: para cada uno de los 775,000 delitos que tenía registrado, mi computadora calculó la distancia que hay entre el lugar donde ocurrió ese delito y cada una de las 195 estaciones de metro. 

Entonces tenemos algo así: 

[delito #1] ---> [distancia entre el delito #1 y la estación #1, distancia entre el delito #1 y la estación #2, ....., distancia entre el delito #1 y la estación 194, distancia entre el delito #1 y la estación 195]

(nota: 195x775,000 = 151'125,000)

Y esto para los 775,000 delitos. Después, mi computadora encontraba el mínimo de esas distancias y así lograba decirme cuál era la estación más cercana para cada delito. La razón por la que necesitaba saber eso es porque más adelante habría de clasificar a las estaciones de metro según su nivel de seguridad, así como dar información de la colonia en la que pertenecen. Más sobre esto en la sección 'Data Analysis.'

Por ahora basta saber que logré hacer ese puente y que en el csv 'delitos_con_estaciones' se puede ver el resultado. 
