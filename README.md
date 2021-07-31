# Examen_Analisis_de_Datos
Bryan Quisaguano Examen de Análisis de Datos
--------------------------------
Como primer paso generamos el código en Jupyter para poder extraer datos, se importan las librerias necesarias para la misma.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/1.JPG" alt="img1"/>
     
Como siguente se realiza el código necesario, declarando variables y asignando el valor de las claves proporcionadas por Twitter.
     
Se usa el método streamlistener para establecer una conexión y transmitiendo datos en tiempo real. 
     
Se construye el archivo json y se lo guarda
     
Posterior a ello se crea una base de datos en CouchDB denomidana "juegosolimpicos", en la cual se guardaran los json generados por la aplicación.
     
Ademas, se ha realizado la extraccion de los datos mediante un Track, y la palabra asignaras fue 'Carapaz'. Una vez se lo ejecuta este lo guardara en la base de datos couchDB.
     
<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/2.JPG" alt="img2"/>
     
Como se observa, al extraer datos en tiempo real de las personas que hablan de Carapaz, en 10 minutos se obtuvo un total de 14 registros.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/3.JPG" alt="img3"/>

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/4.JPG" alt="img4"/>

     
Mediante localizacion
------------------------------------------
El código anterior se puede reutilizar, solo se cambiaria la ultima parte y en lugar de colocar un track se coloca un locations.

Como primer localizacion se ha asignado a Quito. y se guardara en una base de datos denominadas juegosolimpicosquito. Dentro de la cual luego de un tiempo se observa que existen 17 elementos.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/5.JPG" alt="img5"/>

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/6.JPG" alt="img6"/>

Cada json se guardara dentro de la misma base de datos en el caso de las ciudades, para su posterior filtro de manera manual en la interfaz de CouchDB
De la misma manera de procede con la localizacion de Guayaquil. Y como se guardo dentro de la misma base de datos ahora se tiene 32 elementos.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/7.JPG" alt="img7"/>

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/8.JPG" alt="img8"/>

Ahora se la ha realizado para la localizacion de la ciudad de Madrid-España. Al igual, ahora nuestra base contiene 62 elementos.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/9.JPG" alt="img9"/>



Web scraping
---------------------------------------

La página seleccionada y es "Olympics.com" la cual es la página oficial de los juegos olímpicos. Nos centraremos en la seccion de noticias.

Como primer paso se llama a todas las librerias necesarias para realizar web scraping, además, se definen 2 funciones las cuales se usaran para ubicar correctamente los datos.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/10.JPG" alt="img10"/>

Se  ubica el responsive y el enalce de donde de extraera la informacion. En este caso es la pagina oficial de los juegos olimpicos en la seccion noticias.

Ademas, se definen la etiqueta contenedora de donde se extraera los datos, y las etiquetas especificas, junto con las clases que la acompañan y definen a la etiqueta.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/11.JPG" alt="img11"/>

se ubican los for para la limpieza de los datos y evitar que aparezcan las etiquetas del html

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/12.JPG" alt="img12"/>

Ahora se observa los datos que han sido extraidos de la pagina de los juegos olimpicos

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/13.JPG" alt="img13"/>

Ahora lo exportamos a modo de csv para su posterior union a mongodb

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/14.JPG" alt="img14"/>

Facebook
-----------------------------------------
Ahora para la obtencion de datos de facebook se ha seleccionado la pagina oficial de los juegos olimpicos, y se ha empleado un código en el cual se coloca las credeciales para realizar una base de datos en couchdb y posteriormente pasarla a MongoDB, con esto se obtienen los datos necesarios para generar un json.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/15.JPG" alt="img15"/>

En total se han extraido 38 documentos o json en la base de datos

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/16.JPG" alt="img16"/>

Tiktok
-----------------------------------
Para tiktok usare el bash de git para generar un scraping y obtener archivos csv de la plataforma, las cuentas seleccionadas, han sido Olympic y 7Olympic cuanta oficial y de los juegos olimpicos y una aficionada respectivamente.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/17.JPG" alt="img17"/>

Los archivos se han extraido con exito

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/18.JPG" alt="img18"/>

Traspaso a MySQL
---------------------------
Para poder emplear esto he usado la herramienta XAMP, para poder habilitar los servidores.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/19.JPG" alt="img19"/>

Ahora se ha importado los archivos csv generados para tiktok en una base de datos nueva, esto se realiza para los 2 csv

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/20.JPG" alt="img20"/>

Se puede evidenciar los resultados

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/21.JPG" alt="img21"/>

MONGODB
----------------------------------
Para el empleo de mongoDB primero se realiza la activacion del servicio en Windows

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/22.JPG" alt="img22"/>

Una vez activado el servicio nos conectamos al mismo y realizamos la importacion de los archivos necesarios, como los csv de las diferentes bases de datos generadas por los anteriores pasos del examen.

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/23.JPG" alt="img23"/>

<img src="https://github.com/BryanArmando/Examen_Analisis_de_Datos/blob/main/im%C3%A1genes/23.JPG" alt="img23"/>

   
