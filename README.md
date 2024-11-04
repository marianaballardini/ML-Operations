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

*Carga y limpieza de datos:* Procesamiento inicial de los datos de películas para hacerlos adecuados para el análisis.

*Análisis exploratorio de datos (EDA):* Gráficas y visualizaciones, incluyendo una nube de palabras de títulos de películas.

*Creación de features: Extracción de características como director, género, país, y el promedio de votos para mejorar las recomendaciones.

*Procesamiento de lenguaje natural (NLP):* Vectorización de resúmenes de películas para encontrar similitudes en el contenido.

*Sistema de recomendación:* Desarrollo de un modelo de recomendación utilizando similitud de coseno para encontrar películas relacionadas.

*Despliegue de API:* Implementación de la API con FastAPI, que permite obtener recomendaciones y otros datos relevantes.

*Deploy en Render:* Despliegue de la API para que esté disponible en línea.

