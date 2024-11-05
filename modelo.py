import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

class ModeloRecomendacion:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.similarity_matrix = None

    def cargar_datos(self, columnas):
        """
        Carga las columnas específicas del dataset necesarias para la operación actual.
        """
        try:
            df = pd.read_parquet(self.dataset_path, columns=columnas)
            return df
        except Exception as e:
            raise ValueError(f"Error al cargar los datos: {e}")

    def preprocesar_datos(self):
        """
        Preprocesa datos para calcular similitudes y escalas.
        """
        df = self.cargar_datos(['title', 'release_date', 'actor_names', 'director_names', 'vote_average', 'features'])
        
        # Normalizar columnas de texto
        df["title"] = df["title"].str.lower()
        df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
        df["actor_names"] = df["actor_names"].str.lower()
        df["director_names"] = df["director_names"].str.lower()
        
        # Escalar la columna 'vote_average'
        df['vote_average_scaled'] = MinMaxScaler().fit_transform(df[['vote_average']])
        
        # Crear la matriz TF-IDF para similitud
        tfidf = TfidfVectorizer(max_features=300)
        feature_matrix = tfidf.fit_transform(df['features'])
        
        # Calcular la matriz de similitud
        self.similarity_matrix = cosine_similarity(feature_matrix)
        
        # Guardar df preprocesado para uso en recomendación
        self.df = df

    def recomendar(self, titulo):
        """
        Recomienda películas similares a partir de un título.
        """
        # Asegurarse de que los datos estén preprocesados antes de usar
        if self.similarity_matrix is None:
            self.preprocesar_datos()
        
        titulo_normalizado = titulo.lower()
        
        if titulo_normalizado not in self.df['title'].values:
            raise ValueError("Título no encontrado")
        
        index = self.df[self.df['title'] == titulo_normalizado].index[0]
        similitudes = self.similarity_matrix[index]
        # Ajustar similitud usando el promedio de similitud y escala de votación
        similitudes = 0.5 * similitudes + 0.5 * (1 - abs(self.df['vote_average_scaled'] - self.df.loc[index, 'vote_average_scaled']))
        top_indices = similitudes.argsort()[::-1][1:6]  # Excluir la película original

        recomendaciones = self.df.iloc[top_indices]['title'].tolist()
        return recomendaciones
