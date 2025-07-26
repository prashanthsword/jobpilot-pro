# scripts/test_image_ocr.py

from backend.image_parse.ocr_utils import extract_text_from_image

image_path = "data/test_images/sample_text_image.png"  # Make sure this image exists
text = extract_text_from_image(image_path)

print("🧾 Extracted Text:\n", text)
