# Parte II: Data Processing.

En esta sección hay pocos archivos. Pero es importante. Recordemos que ninguna parte del proyecto hubiera funcionado sin una manera de relacionar la base de datos que contiene los delitos con la base de datos de las estaciones de metro. En esta sección logré encontrar tal puente. 

## La fórmula del haversine. 

La forma en que logré esto es usando [la fórmula del haversine](https://es.wikipedia.org/wiki/Fórmula_del_haversine), que te permite encontrar la distancia entre dos pares de coordenadas geográficas; es decir, dos pares de números en la forma (latitud, longitud). 

Para cada uno de los 800,000 delitos en la base de datos, encontré la estación de metro más cercana y así pude crear un nuevo DataFrame con toda la información que necesitaba. En el csv 'delitos_con_estaciones' yace el resultado. 

En la parte III, Data Analyisis, explico cómo transformé esta información en métricas útiles que habrían de darle a nuestro proyecto el contenido que buscábamos ofrecer. 
