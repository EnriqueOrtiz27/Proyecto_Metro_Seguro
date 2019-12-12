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

Este fue el inciso más retador. En el Notebook 'Analizando horas más peligrosas' se encuentra el procedimiento a detalle. Básicamente me vi obligado a determinar, para cada estación, qué porcentaje de los crímenes que se han realizado en esa estación han ocurrido en cada hora. Ver el Notebook para una explicación más clara.  



