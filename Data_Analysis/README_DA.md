# Parte III: Análisis de Datos. 

Esta es la parte más interesante. Una vez que limpié mis bases de datos y las ordené como mejor me parecía, me dediqué a realizar el análisis cuantitivo y cualitativo que habría de darle sazón a nuestro proyecto. 

La parte III se puede dividir en las siguientes cuatro partes. 

## Análisis por Estaciones

Lo primero que hice fue determinar cuáles son las estaciones más seguras y cuáles son las más peligrosas. En el Notebook 'Análisis por estaciones -v2' está detallado el procedimiento con el que realicé esta segmentación. A cada estación le di una calificación del 1-100, en donde 100 significa seguridad extrema y 0, pues, peligro extremo. Además de esto, le asigné a cada estación una posición del 1-180, donde los metros con posición 1 son los más seguros (hubo varios empates, se detalla en el Notebook el porqué) y el metro con la posición 180 es el último en la carrera a la seguridad. 

## Análisis por Colonias

Muy similar al proceso que realicé en el inciso anterior. Determiné qué tan segura o insegura es cada colonia y las ordené según esa calificación. 

## Análisis Afluencia Metro

Para cada estación de metro obtuve el promedio de visitantes al día. La base de datos original está en el archivo afluencia-diaria-del-metro-cdmx y es proveída gratuitamente por el gobierno. 

## Análisis Horas más Peligrosas

Este fue el inciso más retador. En el Notebook 'Analizando horas más peligrosas' se encuentra el procedimiento a detalle. Básicamente me vi obligado a determinar, para cada estación, qué porcentaje de los crímenes realizados en esa estación han ocurrido a cada hora. (Por ejemplo, si en la estación 1 el 20% de los crímenes ocurrieron a las 9 a.m. y el resto a las 11 a.m., entonces mi base de datos tendría un valor de .20 en la columna 'hora_9', .80 en la columna 'hora_11' y .0 en el resto de las columnas. Ver el Notebook para mayor información.)  



