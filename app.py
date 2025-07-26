import streamlit as st
import fitz  # PyMuPDF for PDF reading
import os
import sys

# Setup path to access backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from cover_letter.generate_letter import generate_cover_letter
from resume_refiner.refiner import generate_feedback
from resume_parser.parser import parse_resume_pdf
from job_matcher.matcher import match_resume_to_jd

st.set_page_config(page_title="JobPilot Pro", layout="wide")
st.title("🚀 JobPilot Pro – GenAI Resume Matcher")

st.sidebar.title("📂 Navigation")
section = st.sidebar.radio("Go to:", [
    "📤 Upload Resume & JD",
    "📊 Match & Score",
    "📝 Cover Letter Generator",
    "📈 Resume Feedback"
])

# Session state to store parsed data
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "parsed_resume" not in st.session_state:
    st.session_state.parsed_resume = None
if "jd_text" not in st.session_state:
    st.session_state.jd_text = ""

# 1️⃣ Upload Section
if section == "📤 Upload Resume & JD":
    st.header("Upload Your Resume & Job Description")

    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    jd_file = st.file_uploader("📄 Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

    if resume_file:
        st.success("✅ Resume uploaded successfully!")
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())

        resume_text, parsed_data = parse_resume_pdf("temp_resume.pdf")
        st.session_state.resume_text = resume_text
        st.session_state.parsed_resume = parsed_data

        st.subheader("🧠 Parsed Resume Data")
        st.json(parsed_data)

    if jd_file:
        if jd_file.type == "application/pdf":
            with fitz.open(stream=jd_file.read(), filetype="pdf") as doc:
                jd_text = "\n".join(page.get_text() for page in doc)
        else:
            jd_text = jd_file.read().decode("utf-8")

        st.success("✅ Job description uploaded!")
        st.session_state.jd_text = jd_text
        st.text_area("📋 Job Description Preview", jd_text, height=200)

# 2️⃣ Match & Score Section
elif section == "📊 Match & Score":
    st.header("LLM-Powered Resume Matching")

    if st.session_state.parsed_resume and st.session_state.jd_text:
        with st.spinner("Analyzing with AI..."):
            score, feedback = match_resume_to_jd(
                st.session_state.parsed_resume, st.session_state.jd_text
            )

        st.metric("🔍 Match Score", f"{score} %")
        st.subheader("🧠 AI Feedback")
        st.write(feedback)
    else:
        st.warning("⚠️ Please upload resume and job description first.")

# 3️⃣ Cover Letter Generator (your working part)
elif section == "📝 Cover Letter Generator":
    st.header("✍️ Generate a Cover Letter with AI")

    if st.session_state.parsed_resume and st.session_state.jd_text:
        with st.spinner("Generating cover letter..."):
            letter = generate_cover_letter(
                st.session_state.parsed_resume, st.session_state.jd_text
            )
        st.text_area("📄 Your Cover Letter", letter, height=300)
    else:
        st.warning("⚠️ Please upload resume and job description first.")

# 4️⃣ Resume Feedback Section
elif section == "📈 Resume Feedback":
    st.header("📋 AI Resume Feedback")

    if st.session_state.resume_text:
        with st.spinner("Analyzing resume with LLM..."):
            feedback = generate_feedback(st.session_state.resume_text)

        st.subheader("💡 Suggestions to Improve Your Resume")
        st.write(feedback)
    else:
        st.warning("⚠️ Please upload a resume first.")
