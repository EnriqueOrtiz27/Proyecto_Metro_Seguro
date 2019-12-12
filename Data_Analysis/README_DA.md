# Parte III: Análisis de Datos. 

Esta es la parte más interesante. Una vez que limpié mis bases de datos y las acomodé como mejor me parecía, me pude dedicar a realizar el análisis cuantitivo y cualitativo que habría de darle sazón a nuestro proyecto. 

Veamos qué hice:

## Análisis por Estaciones

Lo primero que hice fue determinar cuáles son las estaciones más seguras y cuáles son las más peligrosas. En el Notebook 'Análisis por estaciones -v2' está detallado el procedimiento con el que realicé esta segmentación. A cada estación le di una calificación del 1-100, en donde 100 significa seguridad extrema y 0, pues, peligro extremo. Además de esto, le asigné a cada estación una posición del 1-180, donde los metros con posición 1 son los más seguros (hubo varios empates, se detalla en el Notebook el porqué) y el metro con la posición 180 es el último en la carrera a la seguridad. 

## Análisis por Colonias

Muy similar al proceso que realicé en el inciso anterior. Determiné qué tan segura o insegura es cada colonia y las ordené según esa calificación. 

## Análisis Afluencia Metro

Para cada estación de metro obtuve el promedio de visitantes al día. La base de datos original está en el archivo afluencia-diaria-del-metro-cdmx y es proveída gratuitamente por el gobierno. 

## Análisis Horas más Peligrosas

Este fue el inciso más retador. En el Notebook 'Analizando horas más peligrosas' se encuentra el procedimiento a detalle. Básicamente me vi obligado a determinar, para cada estación, qué porcentaje de los crímenes que se han realizado en esa estación han ocurrido en cada hora. 

Por ejemplo, si la estación X tiene 100 crímenes al día, 10 por cada hora entre las 10 a.m. y las 8 p.m. entonces tendría algo así en la base de datos:

nombre_estacion     hora_5  hora_6 hora_7 hora_8 hora_9 hora_10 hora_11 hora_12 ...... hora_20 hora_21 hora_22 hora_23 

estacion X            0.0     0.0    0.0    0.0    0.0    0.10    .10     .10            0.0      0.0     0.0    0.0 


Notar cómo el .10 significa que el 10% de los crímenes de esa estación ocurrieron a esas horas. Notar también que la hora 20 (8 p.m) tiene el 0% porque para entonces ya *transcurrieron* diez horas (si los delitos empezaron a las 10 de la mañana, tenemos entonces: 10, 11, 12, 1, 2, 3, 4, 5, 6 y 7).



