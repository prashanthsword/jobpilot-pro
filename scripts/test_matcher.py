# scripts/test_matcher.py
import sys
import os
sys.path.append(os.path.abspath("."))

from backend.core.resume_matcher import match_resume_with_jd

sample_resume = """
Experienced AI/ML engineer with projects in skin disease classification, resume matching, and chatbot assistants.
Skilled in Python, TensorFlow, OpenAI, Streamlit, and deep learning.
"""

sample_jd = """
We are looking for a resume parser developer skilled in OpenAI, NLP, and AI model integration. 
Experience with PDF extraction, embedding generation, and ATS-friendly resume scoring preferred.
"""

score, feedback = match_resume_with_jd(sample_resume, sample_jd)

print(f"\n✅ Match Score: {score}%")
print(f"\n🧠 Feedback:\n {feedback}")
