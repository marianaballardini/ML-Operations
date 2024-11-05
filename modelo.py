import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

class ModeloRecomendacion:
    def __init__(self, dataset_path):
        # Cargar el dataset
        self.df = pd.read_parquet(dataset_path)
        self.preprocesar_datos()

    def preprocesar_datos(self):
        # Normalizar mayúsculas/minúsculas
        self.df["title"] = self.df["title"].str.lower()
        self.df["release_date"] = pd.to_datetime(self.df["release_date"], errors='coerce')
        self.df["actor_names"] = self.df["actor_names"].str.lower()
        self.df["director_names"] = self.df["director_names"].str.lower()

        # Escalar la columna 'vote_average'
        self.df['vote_average_scaled'] = MinMaxScaler().fit_transform(self.df[['vote_average']])
        
        # Crear la matriz TF-IDF
        tfidf = TfidfVectorizer(max_features=300)
        feature_matrix = tfidf.fit_transform(self.df['features'])
        
        # Calcular la matriz de similitud
        self.similarity_matrix = cosine_similarity(feature_matrix)

    def recomendar(self, titulo):
        """Recomienda películas similares a partir de un título."""
        titulo_normalizado = titulo.lower()
        
        if titulo_normalizado not in self.df['title'].values:
            raise ValueError("Título no encontrado")
        
        index = self.df[self.df['title'] == titulo_normalizado].index[0]
        similitudes = self.similarity_matrix[index]
        similitudes = 0.5 * similitudes + 0.5 * (1 - abs(self.df['vote_average_scaled'] - self.df.loc[index, 'vote_average_scaled']))
        top_indices = similitudes.argsort()[::-1][1:6]  # Excluir la película original

        recomendaciones = self.df.iloc[top_indices]['title'].tolist()
        return recomendaciones
