# Parte III: Análisis de Datos. 

Esta es la parte más interesante. Una vez que limpié mis bases de datos y las ordené como mejor me parecía, me dediqué a realizar el análisis cuantitivo y cualitativo necesario para nuestra aplicación. 

La parte III se puede dividir en cuatro.

## Clasificación de Estaciones

Lo primero que hice fue determinar cuáles son las estaciones más seguras y cuáles son las más peligrosas. En el Notebook 'Análisis por estaciones -v2' se detalla la forma en que procedí. Al final de este proceso, pude determinar una califación del 1-100 para el nivel de seguridad de las estaciones y el ranking de cada una respecto a las demás. 

## Clasificación de Colonias

Proceso similar que realicé en el inciso anterior. Determiné qué tan segura o insegura es cada colonia y las ordené acordemente.

## Análisis de la Afluencia

Para cada estación de metro obtuve el promedio de visitantes al día. La base de datos original está en el archivo afluencia-diaria-del-metro-cdmx y es proveída gratuitamente por el gobierno. 

## Análisis por Horarios

Este fue el inciso más retador. En el Notebook 'Analizando horas más peligrosas' se detalla la forma en que procedí. Para cada estación, obtuve la proporción del total de delitos ocurridos en esa estación para cada una de las horas de operación. (Por ejemplo, el resultado está en la forma:  25% de todos los crímenes en la estación del Zócalo han sido entre 8-9 a.m., otro 10% ha sido a las 12 del día, un 25% ha sido de 2-3 p.m y el 40% restante entre 6-7 p.m.) 

Este inciso fue importante porque permitió que nuestra aplicación tuviera el *feature* más importante, y que nos distingue como únicos: un histograma que muestra las horas más seguras y las más inseguras para cada estación (parecido al que está en el README principal del REPO). 


