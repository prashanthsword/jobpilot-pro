# scripts/test_full_resume_analysis.py

from backend.utils.file_utils import extract_text_from_file
from backend.ats_scoring.ats_score import ats_score
from backend.core.resume_matcher import match_resume_with_jd
from backend.cover_letter.generate_letter import generate_cover_letter

import os

# Set your file paths here
resume_path = "data/data_resumes/sample_resume.pdf"
jd_path = "data/data_jds/sample_jd.txt"

# === Load files ===
with open(resume_path, "rb") as f:
    resume_text = extract_text_from_file(f)

with open(jd_path, "r", encoding="utf-8") as f:
    job_description = f.read()

# === ATS Score ===
print("\n📊 ATS Score:")
score, missing_keywords = ats_score(resume_text, job_description)
print(f"Score: {score:.2f}%")
print("Missing Keywords:", missing_keywords)

# === Resume Matching ===
print("\n📈 Resume–JD Match:")
match_score, feedback = match_resume_with_jd(resume_text, job_description)
print(f"Match Score: {match_score:.2f}%")
print("Feedback:", feedback)

# === Cover Letter ===
print("\n✍️ Generating Cover Letter (LLaMA3)...")
cover_letter = generate_cover_letter(resume_text, job_description)
print("\n📄 Cover Letter:\n")
print(cover_letter)
