### Machine Learning Operations (MLOps) ###

El proyecto consiste en crear un sistema de recomendación de películas basado en análisis de datos y machine learning. Incluye una API implementada con FastAPI para consultar recomendaciones y otros datos relevantes.


### Sistema de Recomendación de Películas ###
Este proyecto utiliza técnicas de procesamiento de lenguaje natural y aprendizaje automático para recomendar películas similares basadas en las preferencias del usuario. Implementado con FastAPI, permite a los usuarios buscar actores y directores, así como obtener recomendaciones personalizadas de películas a través de una API.




**Tecnologías utilizadas:**

Python

FastAPI

Pandas

Scikit-learn

Uvicorn




__Características:__

- Búsqueda de información sobre actores y directores.

- Recomendaciones personalizadas basadas en similitudes de películas.

- API ligera y eficiente para integración.




__Instrucciones de uso:__

- Clona el repositorio.

- Instala las dependencias con _pip install -r requirements.txt._

- Ejecuta la API con _uvicorn api:app --reload_




**Características del Proyecto**

<u> Carga y limpieza de datos:</u> Procesamiento inicial de los datos de películas para hacerlos adecuados para el análisis.

<u>Análisis exploratorio de datos (EDA):</u> Gráficas y visualizaciones, incluyendo una nube de palabras de títulos de películas.

<u>Creación de features:</u> Extracción de características como director, género, país, y el promedio de votos para mejorar las recomendaciones.

<u>Procesamiento de lenguaje natural (NLP):</u> Vectorización de resúmenes de películas para encontrar similitudes en el contenido.

<u>Sistema de recomendación:</u> Desarrollo de un modelo de recomendación utilizando similitud de coseno para encontrar películas relacionadas.

<u>Despliegue de API:</u> Implementación de la API con FastAPI, que permite obtener recomendaciones y otros datos relevantes.

<u>Deploy en Render:</u> Despliegue de la API para que esté disponible en línea.


**Endpoints disponibles**

**Cantidad de filmaciones por mes:**  

URL: /cantidad_filmaciones_mes/{mes}  

Método: GET  

Parámetros: mes (str): Nombre del mes en español (ej. "enero").  

Respuesta: Número de películas estrenadas en el mes especificado.  



**Cantidad de filmaciones por día:**  

URL: /cantidad_filmaciones_dia/{dia}  

Método: GET  

Parámetros: dia (str): Nombre del día en español (ej. "lunes").  

Respuesta: Número de películas estrenadas en el día especificado.  


**Score de un título:**  

URL: /score_titulo/{titulo}  

Método: GET  

Parámetros: titulo (str): Título de la película.  

Respuesta: Año de estreno y score de la película.  



**Votos de un título:**  

URL: /votos_titulo/{titulo}  

Método: GET  

Parámetros: titulo (str): Título de la película.  

Respuesta: Información sobre el total de votos y promedio.  



**Información de un actor:**  

URL: /actor/{nombre_actor}  

Método: GET  

Parámetros: nombre_actor (str): Nombre del actor.  

Respuesta: Información sobre las películas del actor.  



**Información de un director:**  

URL: /get_director/{nombre_director}  

Método: GET  

Parámetros: nombre_director (str): Nombre del director.  

Respuesta: Lista de películas del director y sus detalles.  



**Recomendación de películas:**  

URL: /recomendacion/{titulo}  

Método: GET  

Parámetros: titulo (str): Título de la película.  

Respuesta: Lista de títulos de películas recomendadas.  



 
  ## Carga y limpieza de datos: ##  

  Se realiza el ETL en dos archivos, uno de peliculas y otro de creditos que contiene información sobre actores y directores.  
  Primeramente se realiza un chequeo para saber que tipo de datos tenemos, si hay nulos, duplicados, etc. 
  


          
         

## EDA ##  

# Distribución de la calificación promedio de las películas por año de estreno: #
En este análisis, exploramos la evolución de las calificaciones de las películas a lo largo de los años utilizando un gráfico de boxplot. Al visualizar la distribución de las calificaciones por año de estreno, pudimos observar que:

Variabilidad consistente: La dispersión de las calificaciones se mantuvo relativamente estable a lo largo del período analizado.
Calificaciones promedio: Si bien hubo fluctuaciones anuales, no identificamos una tendencia clara de aumento o disminución en las calificaciones promedio.
Valores atípicos: Notamos la presencia de algunas películas con calificaciones excepcionalmente altas o bajas en cada año, lo que sugiere la existencia de títulos que sobresalen o quedan por debajo de las expectativas generales.
A partir de estos hallazgos, podemos concluir que, en general, la calidad percibida de las películas, según las calificaciones, ha mantenido un nivel relativamente constante a lo largo de los años. Sin embargo, es importante considerar que este análisis se basa en un conjunto de datos específico y que otros factores, como los géneros cinematográficos, las plataformas de distribución o los cambios en los hábitos de consumo, podrían influir en los resultados."

# Gráfico de dispersión entre vote_average y revenue #  













Análisis del Gráfico de barras 
El gráfico muestra la distribución de películas por género. Cada barra representa un género y su altura indica la cantidad de películas que pertenecen a ese género.

Observaciones clave:

Géneros más populares: Se pueden identificar claramente los géneros con mayor cantidad de películas. Estos son los que tienen las barras más altas.
Géneros menos populares: Los géneros con menos películas se representan con barras más cortas.
Distribución: La distribución de películas entre los géneros no parece ser uniforme. Algunos géneros tienen una representación mucho mayor que otros.


enfatiza que elegiste estas características por su relevancia conceptual y no solo por su correlación estadística. Puedes mencionar que, aunque género, director y país no tengan una correlación numérica fuerte, juegan un papel clave en el gusto de los usuarios, lo cual es fundamental para recomendaciones basadas en similitudes de contenido.



  


