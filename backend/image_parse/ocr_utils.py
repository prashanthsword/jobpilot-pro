# backend/image_parse/ocr_utils.py

import pytesseract
from PIL import Image
import os

# Optional: Set path manually if tesseract is not in PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str) -> str:
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"[ERROR] Failed to extract text: {str(e)}"
