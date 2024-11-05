from fastapi import FastAPI, HTTPException
import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Inicializar FastAPI
app = FastAPI()

# Cargar el dataset
df = pd.read_parquet("dataset_ok.parquet")

# Normalizar mayúsculas/minúsculas para ciertas columnas que usaremos en las consultas
df["title"] = df["title"].str.lower()
df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')  # Convertir release_date a datetime
df["actor_names"] = df["actor_names"].str.lower()
df["director_names"] = df["director_names"].str.lower()

# Función para normalizar texto eliminando tildes y caracteres diacríticos
def normalizar_texto(texto: str) -> str:
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')

# 1. Endpoint para cantidad de filmaciones por mes
@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3,
        "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9,
        "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    mes_normalizado = normalizar_texto(mes.lower())
    mes_num = meses.get(mes_normalizado)
    
    if mes_num is None:
        raise HTTPException(status_code=404, detail="Mes no válido")
    
    cantidad = df[df["release_date"].dt.month == mes_num].shape[0]
    return {"mensaje": f"{cantidad} películas fueron estrenadas en el mes de {mes.capitalize()}"}

# 2. Endpoint para cantidad de filmaciones por día
@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    dias = {
        "lunes": 0, "martes": 1, "miercoles": 2,
        "jueves": 3, "viernes": 4, "sabado": 5, "domingo": 6
    }
    dia_normalizado = normalizar_texto(dia.lower())
    dia_num = dias.get(dia_normalizado)
    
    if dia_num is None:
        raise HTTPException(status_code=404, detail="Día no válido")
    
    cantidad = df[df["release_date"].dt.dayofweek == dia_num].shape[0]
    return {"mensaje": f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"}

# 3. Endpoint para score de un título
@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str):
    titulo_normalizado = normalizar_texto(titulo.lower())
    pelicula = df[df["title"] == titulo_normalizado]
    
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    
    resultado = pelicula.iloc[0]
    return {
        "mensaje": f"La película {titulo.capitalize()} fue estrenada en el año {resultado['release_year']} con un score de {resultado['vote_average']}"
    }

# 4. Endpoint para votos de un título
@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str):
    titulo_normalizado = normalizar_texto(titulo.lower())
    pelicula = df[df["title"] == titulo_normalizado]
    
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    
    resultado = pelicula.iloc[0]
    
    if resultado["vote_count"] < 2000:
        raise HTTPException(status_code=400, detail="La película no cumple con el mínimo de 2000 valoraciones")
    
    return {
        "mensaje": f"La película {titulo.capitalize()} fue estrenada en el año {resultado['release_year']}. "
                   f"La misma cuenta con un total de {resultado['vote_count']} valoraciones, con un promedio de {resultado['vote_average']}"
    }


#5 Endpoint información de actor

@app.get("/actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    """
    Busca información sobre un actor en la base de datos y calcula estadísticas.

    Args:
        nombre_actor (str): Nombre del actor a buscar.

    Returns:
        dict: Un diccionario con la información del actor o un mensaje de error.
    """

    # Normalizar el nombre del actor
    nombre_actor_normalizado = normalizar_texto(nombre_actor.lower())

    # Filtrar si el actor está listado únicamente en 'actor_names'
    es_solo_actor = (df['actor_names'].str.contains(nombre_actor_normalizado, case=False, na=False)).any() and \
                   not (df['director_names'].str.contains(nombre_actor_normalizado, case=False, na=False)).any()

    if not es_solo_actor:
        return {"mensaje": "El actor buscado no está en la base de datos o es ademas director, por lo que se excluye del análisis."}

    peliculas_actor = df[df['actor_names'].str.contains(nombre_actor_normalizado, case=False, na=False)]

    # Calcular estadísticas
    cantidad_peliculas = len(peliculas_actor)
    retorno_total = peliculas_actor["return"].sum()
    promedio_retorno = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0

    return {
        "mensaje": f"El actor {nombre_actor.capitalize()} ha participado en {cantidad_peliculas} películas, "
                   f"con un retorno total de {retorno_total} y un promedio de retorno de {promedio_retorno:.2f} por película"
    }

# 6. Endpoint para información de un director
@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    # Normalizamos el nombre del director a minúsculas y eliminamos caracteres diacríticos
    nombre_director_normalizado = normalizar_texto(nombre_director.lower())
    
    # Buscamos el director en la columna director_names
    # Utilizamos str.contains para permitir que aparezca el director aunque haya nombres adicionales
    peliculas_director = df[df["director_names"].str.contains(nombre_director_normalizado, na=False)]
    
    if peliculas_director.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    
    info_peliculas = []
    
    for _, pelicula in peliculas_director.iterrows():
        info_peliculas.append({
            "titulo": pelicula["title"].capitalize(),
            "fecha": pelicula["release_date"].date(),
            "retorno": pelicula["return"],
            "costo": pelicula["budget"],
            "ganancia": pelicula["revenue"] - pelicula["budget"]
        })
    
    return {
        "mensaje": f"El director {nombre_director.capitalize()} tiene las siguientes películas:",
        "peliculas": info_peliculas
    }

# 7. Endpoint para recomendaciones
# Preprocesamiento
# Escalar `vote_average` entre 0 y 1

df['vote_average_scaled'] = MinMaxScaler().fit_transform(df[['vote_average']])

# Vectorizar `features`
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(df['features'])

# Crear matriz de similitud para `features`
similarity_matrix = cosine_similarity(feature_matrix)

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):
    """
    Recomienda películas similares a partir de un título.

    Args:
        titulo (str): Título de la película.

    Returns:
        dict: Diccionario con la lista de títulos de películas recomendadas.
    """
    # Verificar si el título existe en el dataset
    if titulo not in df['title'].values:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    
    # Obtener el índice de la película
    index = df[df['title'] == titulo].index[0]

    # Obtener las similitudes de la película
    similitudes = similarity_matrix[index]

    # Combinar con similitud de puntuación
    similitudes = 0.5 * similitudes + 0.5 * (1 - abs(df['vote_average_scaled'] - df.loc[index, 'vote_average_scaled']))

    # Obtener los índices de las películas más similares
    top_indices = similitudes.argsort()[::-1][1:6]  # Excluir la película original

    # Retornar los títulos de las películas recomendadas
    recomendaciones = df.iloc[top_indices]['title'].tolist()
    
    return {
        "mensaje": f"Recomendaciones para la película '{titulo}':",
        "recomendaciones": recomendaciones
    }