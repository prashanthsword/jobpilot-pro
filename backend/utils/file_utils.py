# backend/utils/file_utils.py

import os
from backend.utils.text_utils import (
    extract_text_from_pdf,
    extract_text_from_txt,
    extract_text_from_docx
)

def extract_text_from_file(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(uploaded_file)
    elif ext == ".txt":
        return extract_text_from_txt(uploaded_file)
    elif ext == ".docx":
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file format.")
