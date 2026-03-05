from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text_list):
    return model.encode(text_list, convert_to_numpy=True)

def extract_key_sentences(text_sections, top_k=5):
    embeddings = get_embeddings(text_sections)
    centroid = np.mean(embeddings, axis=0)
    scores = [np.dot(e, centroid) for e in embeddings]
    ranked = np.argsort(scores)[::-1]
    return [text_sections[i] for i in ranked[:top_k]]