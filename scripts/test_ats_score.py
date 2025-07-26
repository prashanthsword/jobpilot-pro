from backend.ats_scoring.ats_score import ats_score

resume_text = """
Experienced AI Engineer with knowledge in Python, Machine Learning, NLP, and Streamlit.
Built multiple AI projects including a resume matcher and interview question generator.
"""

jd_text = """
Looking for a candidate with experience in NLP, resume parsing, ATS integration, and machine learning.
Preferred: Streamlit or Gradio for UI.
"""

score, missing = ats_score(resume_text, jd_text)

print(f"📊 ATS Score: {score}%")
print("\n🚫 Missing Keywords:")
for kw in missing:
    print(f" - {kw}")
