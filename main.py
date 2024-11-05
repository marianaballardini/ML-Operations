from fastapi import FastAPI, HTTPException
import pandas as pd
import unicodedata

app = FastAPI()

# Normalizar texto eliminando tildes y caracteres diacríticos
def normalizar_texto(texto: str) -> str:
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')

# Método para cargar solo las columnas necesarias bajo demanda
def cargar_datos(columnas):
    return pd.read_parquet("dataset_ok.parquet", columns=columnas)

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
    
    df = cargar_datos(["release_date"])
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
    
    df = cargar_datos(["release_date"])
    cantidad = df[df["release_date"].dt.dayofweek == dia_num].shape[0]
    return {"mensaje": f"{cantidad} películas fueron estrenadas en los días {dia.capitalize()}"}

# 3. Endpoint para score de un título
@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str):
    titulo_normalizado = normalizar_texto(titulo.lower())
    df = cargar_datos(["title", "release_year", "vote_average"])
    pelicula = df[df["title"].str.lower() == titulo_normalizado]
    
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    
    resultado = pelicula.iloc[0]
    return {
        "mensaje": f"La película {titulo.capitalize()} fue estrenada en el año {resultado['release_year']} con un score de {resultado['vote_average']}"
    }

# Resto de los endpoints... (similar estructura usando cargar_datos(["columnas necesarias"]))
