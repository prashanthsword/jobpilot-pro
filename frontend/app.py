# final app.py inside frontend/app.py
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.utils.file_utils import extract_text_from_file
from backend.ats_scoring.ats_score import ats_score
from backend.ats_scoring.ats_improver import suggest_resume_improvements
from backend.core.resume_matcher import match_resume_with_jd
from backend.cover_letter.generate_letter import generate_cover_letter
from backend.interview_agent.agent import generate_interview_questions
from backend.language_tools.grammar_corrector import correct_grammar
from backend.language_tools.summarizer import summarize_text
from backend.language_tools.paraphraser import paraphrase_text
from backend.resume_refiner.refiner import generate_resume_improvements_llama
from backend.utils.pdf_utils import save_cover_letter_to_pdf
from backend.jd_scraper.scraper import get_job_description
from backend.voice_bot.llama_utils import get_llama_response

st.set_page_config(page_title="JobPilot Pro", layout="wide")
st.title("🧠 JobPilot Pro - GenAI Career Copilot")

# Shared session state
def init_state():
    for key in ["resume_text", "jd_text", "generated_letter", "grammar_checked", "summary", "paraphrased", "llama_tips", "interview_questions", "llama_response"]:
        if key not in st.session_state:
            st.session_state[key] = ""
init_state()

# Tab layout
tabs = st.tabs([
    "📤 Upload Resume + JD", "📊 ATS Insights", "📝 Cover Letter",
    "🎯 Resume Tips", "🎙️ Interview Qs", "🧠 Ask LLaMA"
])

# 1. Upload Resume + JD
with tabs[0]:
    st.header("📤 Upload Your Resume & Job Description")
    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume (PDF/DOCX/TXT)", type=["pdf", "txt", "docx"])
        if resume_file:
            st.session_state.resume_text = extract_text_from_file(resume_file)
            st.success("✅ Resume uploaded!")
            st.text_area("🧾 Resume Text", st.session_state.resume_text, height=200)

    with col2:
        jd_file = st.file_uploader("Upload Job Description (PDF/DOCX/TXT)", type=["pdf", "txt", "docx"])
        if jd_file:
            st.session_state.jd_text = extract_text_from_file(jd_file)
            st.success("✅ JD uploaded!")
            st.text_area("📃 JD Text", st.session_state.jd_text, height=200)

        jd_url = st.text_input("Or paste JD URL (LinkedIn/Naukri/...):")
        if st.button("🔗 Fetch JD from URL") and jd_url:
            st.session_state.jd_text = get_job_description(jd_url)
            st.text_area("📃 JD Text (Scraped)", st.session_state.jd_text, height=200)

# 2. ATS Insights
with tabs[1]:
    st.header("📊 ATS Matching Insights")
    if st.session_state.resume_text and st.session_state.jd_text:
        score, missing = ats_score(st.session_state.resume_text, st.session_state.jd_text)
        match, feedback = match_resume_with_jd(st.session_state.resume_text, st.session_state.jd_text)

        st.metric("✅ ATS Score", f"{score}%")
        st.metric("📈 Match Score", f"{match}%")

        if feedback:
            st.warning(feedback[0])

        with st.expander("🔍 Missing Keywords"):
            st.write(missing[:20])

        suggestions = suggest_resume_improvements(st.session_state.resume_text, st.session_state.jd_text)
        if suggestions:
            st.info("💡 Resume should include: " + ", ".join(suggestions))
    else:
        st.warning("Upload both resume and JD to view insights.")

# 3. Cover Letter Generator
with tabs[2]:
    st.header("📝 AI-Powered Cover Letter")
    if st.session_state.resume_text and st.session_state.jd_text:
        if st.button("✍️ Generate Cover Letter"):
            st.session_state.generated_letter = generate_cover_letter(st.session_state.resume_text, st.session_state.jd_text)
        if st.session_state.generated_letter:
            st.text_area("📄 Generated Cover Letter", st.session_state.generated_letter, height=300)
            if st.button("📄 Download as PDF"):
                save_cover_letter_to_pdf(st.session_state.generated_letter, "cover_letter.pdf")
                with open("cover_letter.pdf", "rb") as f:
                    st.download_button("📥 Download Cover Letter PDF", f, file_name="cover_letter.pdf")
    else:
        st.warning("Please upload resume and JD first.")

# 4. Resume Tips
with tabs[3]:
    st.header("🎯 Resume Grammar & Tips")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Grammar Check"):
            st.session_state.grammar_checked = correct_grammar(st.session_state.resume_text)
        if st.session_state.grammar_checked:
            st.text_area("✅ Corrected Resume", st.session_state.grammar_checked, height=200)

        if st.button("📚 Summarize JD"):
            st.session_state.summary = summarize_text(st.session_state.jd_text)
        if st.session_state.summary:
            st.text_area("🧾 JD Summary", st.session_state.summary, height=200)

    with col2:
        input_line = st.text_area("✏️ Enter sentence to paraphrase:")
        if st.button("🔁 Paraphrase"):
            st.session_state.paraphrased = paraphrase_text(input_line)
        if st.session_state.paraphrased:
            st.text_area("🪄 Paraphrased", st.session_state.paraphrased, height=150)

        if st.button("🔧 Resume Improvement by LLaMA"):
            st.session_state.llama_tips = generate_resume_improvements_llama(st.session_state.resume_text, st.session_state.jd_text)
        if st.session_state.llama_tips:
            st.text_area("📌 AI Resume Tips", st.session_state.llama_tips, height=200)

# 5. Interview Qs
with tabs[4]:
    st.header("🎙️ Interview Questions Generator")
    if st.button("🎤 Generate Interview Questions"):
        st.session_state.interview_questions = generate_interview_questions(st.session_state.resume_text, st.session_state.jd_text)
    if st.session_state.interview_questions:
        st.text_area("🤖 LLaMA Interview Qs", st.session_state.interview_questions, height=250)

# 6. LLaMA Chat
with tabs[5]:
    st.header("🧠 Ask LLaMA Anything")
    user_prompt = st.text_area("💬 Your Prompt to LLaMA")
    if st.button("🧠 Respond"):
        with st.spinner("Thinking..."):
            st.session_state.llama_response = get_llama_response(user_prompt)
    if st.session_state.llama_response:
        st.text_area("🧠 Response", st.session_state.llama_response, height=300)

st.sidebar.success("✅ All modules loaded. Your AI Career Copilot is ready.")