import re

def suggest_resume_improvements(resume_text, jd_text):
    resume_words = set(re.findall(r'\w+', resume_text.lower()))
    jd_words = set(re.findall(r'\w+', jd_text.lower()))
    missing_keywords = jd_words - resume_words

    common_keywords = ["skills", "experience", "python", "machine", "learning", "team", "project",
                       "communication", "problem", "solving", "ai", "deep", "resume", "parser",
                       "gradio", "openai", "llm", "integration"]

    suggestions = [word for word in missing_keywords if word in common_keywords]
    return suggestions
