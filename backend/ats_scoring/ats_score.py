# backend/ats_scoring/ats_score.py

from sklearn.feature_extraction.text import TfidfVectorizer

def ats_score(resume_text: str, job_description: str):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description])

    # Calculate cosine similarity and convert to percentage
    score = (vectors * vectors.T).toarray()[0, 1] * 100

    # Find keywords missing from resume
    resume_tokens = set(resume_text.lower().split())
    jd_tokens = set(job_description.lower().split())
    missing_keywords = list(jd_tokens - resume_tokens)

    return round(score, 2), missing_keywords
