from backend.embeddings.embed_utils import get_embedding
from backend.embeddings.similarity import cosine_similarity

resume = "Experienced Python developer with expertise in NLP and ML."
jd = "Looking for a Python engineer skilled in machine learning and NLP."

embed_resume = get_embedding(resume)
embed_jd = get_embedding(jd)

score = cosine_similarity(embed_resume, embed_jd)
print(f"🔍 Similarity Score: {score * 100:.2f}%")
