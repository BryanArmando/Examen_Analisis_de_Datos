# Examen_Analisis_de_Datos
Bryan Quisaguano Examen de Análisis de Datos
--------------------------------
Como primer paso generamos el código en Jupyter para poder extraer datos, se importan las librerias necesarias para la misma.
<img
     
Como siguente se realiza el código necesario, declarando variables y asignando el valor de las claves proporcionadas por Twitter.
     
Se usa el método streamlistener para establecer una conexión y transmitiendo datos en tiempo real. 
     
Se construye el archivo json y se lo guarda
     
Posterior a ello se crea una base de datos en CouchDB denomidana "juegosolimpicos", en la cual se guardaran los json generados por la aplicación.
     
Ademas, se ha realizado la extraccion de los datos mediante un Track, y la palabra asignaras fue 'Carapaz'. Una vez se lo ejecuta este lo guardara en la base de datos couchDB.
     
img
     
Como se observa, al extraer datos en tiempo real de las personas que hablan de Carapaz, en 10 minutos se obtuvo un total de 14 registros.
<img
<img
     
Mediante localizacion
------------------------------------------
El código anterior se puede reutilizar, solo se cambiaria la ultima parte y en lugar de colocar un track se coloca un locations.

Como primer localizacion se ha asignado a Quito. y se guardara en una base de datos denominadas juegosolimpicosquito. Dentro de la cual luego de un tiempo se observa que existen 17 elementos.

<img
<img

Cada json se guardara dentro de la misma base de datos en el caso de las ciudades, para su posterior filtro de manera manual en la interfaz de CouchDB
De la misma manera de procede con la localizacion de Guayaquil. Y como se guardo dentro de la misma base de datos ahora se tiene 32 elementos.
<img
<img

Ahora se la ha realizado para la localizacion de la ciudad de Madrid-España. Al igual, ahora nuestra base contiene 62 elementos.
<img
<img>

Web scraping
---------------------------------------

La página seleccionada y es "Olympics.com" la cual es la página oficial de los juegos olímpicos. Nos centraremos en la seccion de noticias.




   
