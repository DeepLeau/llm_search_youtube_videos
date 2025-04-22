import os
import numpy as np
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY) 
SIMILARITIES_RESULTS_THRESHOLD = 0.75

def calculate_cosine_similarity(vector1, vector2):
    if len(vector1) > len(vector2):
        vector2 = np.pad(vector2, (0, len(vector1) - len(vector2)), 'constant')
    elif len(vector2) > len(vector1):
        vector1 = np.pad(vector1, (0, len(vector2) - len(vector1)), 'constant')
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

def get_videos(df, query, number_of_rows=10):
    video_vectors = df.copy()

    response = client.embeddings.create(
    model="text-embedding-ada-002",
    input=query)

    embedding = response.data[0].embedding

    video_vectors["similarity"] = video_vectors["ada_v2"].apply(
        lambda x: calculate_cosine_similarity(np.array(embedding), np.array(x))
    )

    mask = video_vectors["similarity"] >= SIMILARITIES_RESULTS_THRESHOLD
    video_vectors = video_vectors[mask].copy()

    video_vectors = video_vectors.sort_values(by="similarity", ascending=False).head(
        number_of_rows
    )

    return video_vectors.head(number_of_rows)

