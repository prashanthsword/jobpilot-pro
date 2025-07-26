import numpy as np
from sentence_transformers import SentenceTransformer

# Load model once (Instructor-XL, all-MiniLM, etc.)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str) -> np.ndarray:
    """
    Generate vector embedding for input text using SentenceTransformer.
    """
    return model.encode(text, convert_to_numpy=True)
