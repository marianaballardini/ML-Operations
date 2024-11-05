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


La API estará disponible en http://127.0.0.1:8000.



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
