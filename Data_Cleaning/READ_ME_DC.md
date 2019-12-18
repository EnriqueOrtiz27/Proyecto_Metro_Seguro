# Parte I: Data Cleaning. 

## Objetivos: 

i) Descargar las bases de datos relevantes, ii) Explorar esas bases de datos y iii) Limpiar esas bases de datos para proceder a la siguiente etapa (Data Processing.)

## Bases de datos:
	
Yo usé tres bases de datos inicialmente. 

La primera está en el archivo 'carpetas-de-investigacion-pgj-cdmx.csv.zip'. Esta es una base de datos con información de crímenes que han ocurrido en la Ciudad de México. La base cuenta con aproximadamente 800,000 registros y para cada registro tenemos aplia información: qué tipo de crimen fue, en qué colonia y calle ocurrió, cuál es la alcaldía, qué día y a qué hora, etc. En el Notebook 'data_wrangling_delitos' exploro la base de datos con más profundidad. Después, en el archivo 'data_cleaning_delitos' me encargo de limpiar la base de datos.


La segunda base de datos está en el archivo 'estaciones-metro.csv'. Esta base es mucho más sencilla y pequeña. Simplemente tenemos los nombres de las 195 estaciones de metro de la CDMX, su ubicación geográfica, así como las líneas con las que tiene correspondencia. Igual que con la primera base de datos, me encargo de explorar y limpiar esta base de datos en los archivos 'data_wrangling_estaciones' y 'data_cleaning_estaciones'. 

La tercera base de datos contiene la afluencia diaria de cada estación del metro, y fue utilizada más adelante (ver la carpeta Data Analysis). 


Nota: las bases de datos provienen todas de los Datos Abiertos de la CDMX y se pueden encontrar [aquí](https://datos.cdmx.gob.mx/pages/home/)
