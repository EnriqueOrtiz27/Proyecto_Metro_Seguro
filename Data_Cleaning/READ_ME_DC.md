# Parte I: Data Cleaning. 

## Objetivos: 

	-Descargar las bases de datos relevantes.
	-Explorar esas bases de datos para descubrir la naturaleza de los datos. 
	-Limpiar esas bases de datos y dejarlas lo más listas para la siguiente etapa (Data Processing.)

## Bases de datos:
	
	Yo usé dos bases de datos inicialmente. 

	La primera está en el archivo 'carpetas-de-investigacion-pgj-cdmx.csv.zip' y 
	consiste en registros con información de delitos que han ocurrido en la CDMX. Esta base de datos es de aproximadamente 800,000 registros y cada registro es un delito distinto. Por cada delito podemos ver dónde fue, qué tipo de delito fue, cuándo fue reportado, etc. En el archivo 'data_wrangling_delitos' exploro la base con más profundidad. Después, en el archivo 'data_cleaning_delitos' me encargo de limpiar esa base y finalmente la guardo (ya limpia) como 'delitos_limpio_v1.csv.zip'. 

	La segunda base de datos está en el archivo 'estaciones-metro.csv'. Esta base es mucho más sencilla y pequeña. Simplemente tenemos los nombres de las 195 estaciones de metro de la CDMX, su ubicación geográfica, así como las líneas con las que hace correspondencia. Igual que con la primera base de datos, me encargo de explorar y limpiar esta base de datos en los archivos 'data_wrangling_estaciones' y 'data_cleaning_estaciones'. Pueden ver cómo quedó al final en el archivo 'estaciones_limpias_v1.csv'. 

