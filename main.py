from fastapi import FastAPI, HTTPException
import unicodedata
from modelo import ModeloRecomendacion

# Inicializar FastAPI
app = FastAPI()

# Crear una instancia del modelo de recomendación
modelo = ModeloRecomendacion("dataset_ok.parquet")

# Normalizar texto eliminando tildes y caracteres diacríticos
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
    
    cantidad = modelo.df[modelo.df["release_date"].dt.month == mes_num].shape[0]
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
    
    cantidad = modelo.df[modelo.df["release_date"].dt.dayofweek == dia_num].shape[0]
    return {"mensaje": f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"}

# 3. Endpoint para score de un título
@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str):
    titulo_normalizado = normalizar_texto(titulo.lower())
    pelicula = modelo.df[modelo.df["title"] == titulo_normalizado]
    
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
    pelicula = modelo.df[modelo.df["title"] == titulo_normalizado]
    
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    
    resultado = pelicula.iloc[0]
    
    if resultado["vote_count"] < 2000:
        raise HTTPException(status_code=400, detail="La película no cumple con el mínimo de 2000 valoraciones")
    
    return {
        "mensaje": f"La película {titulo.capitalize()} fue estrenada en el año {resultado['release_year']}. "
                   f"La misma cuenta con un total de {resultado['vote_count']} valoraciones, con un promedio de {resultado['vote_average']}"
    }

# 5. Endpoint información de actor
@app.get("/actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    """Busca información sobre un actor en la base de datos y calcula estadísticas."""
    nombre_actor_normalizado = normalizar_texto(nombre_actor.lower())

    es_solo_actor = (modelo.df['actor_names'].str.contains(nombre_actor_normalizado, case=False, na=False)).any() and \
                   not (modelo.df['director_names'].str.contains(nombre_actor_normalizado, case=False, na=False)).any()

    if not es_solo_actor:
        return {"mensaje": "El actor buscado no está en la base de datos o es además director, por lo que se excluye del análisis."}

    peliculas_actor = modelo.df[modelo.df['actor_names'].str.contains(nombre_actor_normalizado, case=False, na=False)]

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
    nombre_director_normalizado = normalizar_texto(nombre_director.lower())
    
    peliculas_director = modelo.df[modelo.df["director_names"].str.contains(nombre_director_normalizado, na=False)]
    
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


