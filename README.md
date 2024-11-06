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



La API estará disponible en:   https://ml-recomendaciones.onrender.com/docs
      

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

# Análisis del Gráfico de barras  #
El gráfico muestra la distribución de películas por género. Cada barra representa un género y su altura indica la cantidad de películas que pertenecen a ese género.

Observaciones clave:

Desigualdad en la distribución: Se observa una gran disparidad en la cantidad de películas por género. Algunos géneros, como la comedia o el drama, tienen una representación mucho mayor que otros, como el western o el musical.
Géneros dominantes: Los géneros con barras más largas son los más populares o los que tienen una mayor producción cinematográfica.  

Géneros minoritarios: Los géneros con barras más cortas son menos comunes o tienen una producción más limitada.


Interpretación:

Este gráfico nos permite visualizar rápidamente cuáles son los géneros cinematográficos más populares y cuáles son menos frecuentes dentro del conjunto de datos analizado. También podemos identificar tendencias generales en la producción cinematográfica, como la predominancia de ciertos géneros sobre otros.

Se observa una clara desigualdad en la representación de los diferentes géneros, con una predominancia de drama/thriller y drama/comedia y una menor presencia de war, history y foreign.

Esta distribución refleja las tendencias generales de la producción cinematográfica, donde ciertos géneros suelen ser más comerciales y atractivos para el público en general. Sin embargo, es importante destacar que esta distribución puede variar dependiendo de la fuente de los datos y del período de tiempo analizado.

# Gráfico de dispersión entre vote_average y revenue #  

Descripción del Gráfico:

Este gráfico de dispersión muestra la relación entre dos variables clave en la industria del cine: la calificación promedio de una película (en el eje X) y sus ingresos totales (en el eje Y). Cada punto en el gráfico representa una película individual.

Interpretación de los Resultados:

No existe una correlación lineal fuerte: A primera vista, es evidente que no hay una relación lineal directa entre la calificación promedio y los ingresos totales. Es decir, una película con una calificación alta no necesariamente genera mayores ingresos, y viceversa.
Dispersión de los datos: Los puntos se encuentran dispersos en todo el gráfico, lo que indica una gran variabilidad en los resultados. Hay películas con calificaciones altas y bajos ingresos, así como películas con calificaciones bajas y altos ingresos.
Concentración de películas con bajos ingresos: Se observa una concentración de puntos en la parte inferior del gráfico, lo que sugiere que la mayoría de las películas tienen ingresos relativamente bajos, independientemente de su calificación.
Algunos casos excepcionales: Existen algunos puntos aislados que representan películas con calificaciones altas y muy altos ingresos. Estas películas podrían considerarse como "éxitos de taquilla" que han logrado combinar calidad y popularidad.  

Conclusiones:

La calificación no es el único factor determinante de los ingresos: Aunque una buena calificación puede contribuir al éxito comercial de una película, no es el único factor. Otros elementos como el presupuesto de marketing, el elenco, el género, la temporada de estreno y las tendencias del mercado también influyen significativamente en los ingresos.
La relación entre calificación e ingresos es compleja: La relación entre estas dos variables es más compleja de lo que podría parecer a primera vista. Existen múltiples factores que interactúan y pueden producir resultados inesperados.
La variabilidad es la norma: La industria cinematográfica es altamente competitiva y los resultados comerciales pueden variar ampliamente, incluso para películas con características similares.





















enfatiza que elegiste estas características por su relevancia conceptual y no solo por su correlación estadística. Puedes mencionar que, aunque género, director y país no tengan una correlación numérica fuerte, juegan un papel clave en el gusto de los usuarios, lo cual es fundamental para recomendaciones basadas en similitudes de contenido.


Comentario Extenso para el README  DISPERSION 3D 
Análisis de la relación entre calificación, cantidad de votos y año de estreno

Este gráfico de dispersión en 3D nos permite visualizar la relación entre tres variables clave en el análisis de películas: el año de estreno, la calificación promedio y la cantidad de votos.

Hallazgos clave:

Distribución temporal: Observamos una concentración de películas en ciertos años, lo que podría indicar tendencias en la producción cinematográfica o en los hábitos de consumo de las audiencias.
Correlación entre calificación y votos: Existe una tendencia general a que las películas con mayor cantidad de votos también tengan calificaciones más altas. Sin embargo, esta relación no es perfecta, y hay muchos casos de películas muy votadas con calificaciones moderadas o incluso bajas.
Variabilidad en las calificaciones: Las calificaciones promedio de las películas varían considerablemente a lo largo de los años y entre diferentes películas, lo que sugiere que otros factores, como el género, el presupuesto o la popularidad de los actores, pueden influir en la percepción de la calidad por parte de la audiencia.
  


