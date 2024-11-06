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

          Para este paso 

   ### ¿Qué es un Boxplot? ###

Un boxplot, también conocido como diagrama de caja y bigotes, es una representación visual que resume la distribución de un conjunto de datos. Proporciona información sobre:

Valores centrales: La mediana (línea dentro de la caja) representa el valor central de los datos.
Dispersión: Los cuartiles inferior y superior (bordes de la caja) muestran la dispersión del 50% central de los datos.
Valores atípicos: Los puntos fuera de los bigotes suelen considerarse valores atípicos.
Interpretando el Boxplot de "vote_average"

En el gráfico que proporcionas, el boxplot muestra la distribución de la variable "vote_average" (promedio de votos). Podemos observar lo siguiente:

Mediana: La mediana se encuentra alrededor de 8, lo que indica que la mitad de las películas tienen un promedio de votos igual o inferior a 8.
Rango intercuartílico (IQR): La caja representa el IQR, que es la diferencia entre el cuartil superior y el cuartil inferior. En este caso, el IQR parece ser relativamente pequeño, lo que sugiere que la mayoría de las películas tienen un promedio de votos similar.
Valores atípicos: Hay algunos valores atípicos por debajo de la mediana, representados por los puntos aislados. Esto podría indicar que hay algunas películas con un promedio de votos significativamente menor que el resto.



  
### ¿Qué es un gráfico de correlación? ###

Es una representación visual de la relación entre diferentes variables numéricas. Cada celda del gráfico muestra un coeficiente de correlación, un número entre -1 y 1 que indica la fuerza y dirección de la relación:

Valores cercanos a 1: Correlación positiva fuerte. Cuando una variable aumenta, la otra también tiende a aumentar.
Valores cercanos a -1: Correlación negativa fuerte. Cuando una variable aumenta, la otra tiende a disminuir.
Valores cercanos a 0: Correlación débil o nula. No hay una relación lineal clara entre las variables.
Interpretando tu Gráfico Específico

En el gráfico, cada celda representa la correlación entre dos variables del conjunto de datos, como "budget", "popularity", "revenue", etc.

Colores: El color de cada celda indica la fuerza y dirección de la correlación. Por ejemplo, el rojo intenso indica una correlación positiva fuerte, mientras que el azul intenso indica una correlación negativa fuerte.  

Valores numéricos: Los números dentro de cada celda son los coeficientes de correlación exactos.  

  
Extracción de Información Relevante para el EDA  

  
Relaciones Fuertes:
Positivas: "budget" y "revenue" parecen tener una fuerte correlación positiva, lo que sugiere que a mayor presupuesto, mayores ingresos.

Valores cercanos a 0: Las celdas con valores cercanos a 0 indican que no hay una relación lineal clara entre las variables.  

  
Patrones Interesantes:
Grupos de variables altamente correlacionadas: ¿Hay grupos de variables que están muy relacionadas entre sí? Esto podría indicar que estás midiendo aspectos similares de tu dataset.

Cómo utilizar esta Información en el EDA
**Selección de variables:** Podemos usar esta información para seleccionar las variables más importantes para el análisis. Por ejemplo, si estamos interesados en predecir los ingresos, nos centraríamos en las variables que tienen una correlación fuerte con "revenue".
**Construcción de modelos:** La correlación puede ayudarnos a identificar qué variables incluir en un modelo de regresión o clasificación.
**Visualización de datos:** Podemos crear otros tipos de visualizaciones, como gráficos de dispersión, para explorar más a fondo las relaciones entre las variables.


### Conclusiones EDA ### 
Basándonos en el gráfico, podemos observar:

- Existe una fuerte correlación positiva entre el presupuesto de una película y sus ingresos, lo que sugiere que las películas con mayor presupuesto tienden a generar más ganancias.
- La popularidad de una película y su número de votos están altamente correlacionados, lo que indica que las películas más populares tienden a recibir más votos.
- La variable 'return' no parece estar fuertemente correlacionada con ninguna otra variable, lo que podría indicar que es una variable más compleja o que requiere un análisis más profundo.

  
Para tener en cuenta:

**La correlación no implica causalidad:** Aunque dos variables estén altamente correlacionadas, no significa necesariamente que una cause la otra. Podría haber una tercera variable subyacente que influya en ambas.
**Consideremos el contexto:** La interpretación de los resultados siempre debe hacerse en el contexto del problema específico que estás tratando de resolver.

    

