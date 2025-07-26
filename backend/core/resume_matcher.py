# backend/core/resume_matcher.py

def match_resume_with_jd(resume_text, job_description):
    feedback = []
    missing_keywords = []

    resume_lower = resume_text.lower()
    for word in job_description.lower().split():
        if word not in resume_lower and word.isalpha():
            missing_keywords.append(word)

    if missing_keywords:
        feedback.append("⚠️ Consider adding relevant experience or keywords related to: **" + ", ".join(missing_keywords[:10]) + "**.")

    match_score = 100 - (len(missing_keywords) / len(job_description.split())) * 100
    return round(match_score, 2), feedback
