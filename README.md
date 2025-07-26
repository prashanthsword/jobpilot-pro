# 🧠 JobPilot Pro - GenAI Career Copilot

> The ultimate AI-powered resume + job assistant built with LLaMA, Streamlit, and Transformers

![streamlit](https://img.shields.io/badge/Streamlit-App-blue)  
🔗 Live Demo: [https://jobpilot-pro.streamlit.app](https://jobpilot-pro.streamlit.app)

---

## 🚀 Features

- 📄 **Resume Parsing** (PDF/DOCX/TXT)
- 📊 **ATS Score Calculator** (TF-IDF, Match %, keyword suggestions)
- ✍️ **LLaMA-powered Cover Letter Generator**
- 🛠️ **Resume Improvement Tips**
- 🧠 **Grammar Correction & JD Summarization**
- 🔁 **Text Paraphrasing**
- 🎙️ **Interview Question Generator**
- 🤖 **Chat with LLaMA** (Ollama)

---

## 🧰 Tech Stack

- `Streamlit` for UI
- `Python` for backend logic
- `HuggingFace Transformers`
- `LLaMA 3 via Ollama` (local inference)
- `PyMuPDF`, `docx`, `language_tool_python`, `scikit-learn`

---

## 📦 Setup Instructions


# Clone repo
git clone https://github.com/prashanthsword/jobpilot-pro.git
cd jobpilot-pro

# Create & activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run frontend/app.py
