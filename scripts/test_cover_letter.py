from backend.cover_letter.generate_letter import generate_cover_letter
from backend.utils.file_utils import load_text
from backend.utils.pdf_utils import save_cover_letter_to_pdf

print("🧠 Generating cover letter locally with LLaMA3...")

resume_text = load_text("data/data_resumes/resume1.txt")
job_description = load_text("data/jds/jd1.txt")

letter = generate_cover_letter(resume_text, job_description)

print("✅ Cover letter generated!")
print("\n📄 Generated Cover Letter:\n")
print(letter)

# Save to text
with open("data/cover_letters/cover_letter1.txt", "w", encoding="utf-8") as f:
    f.write(letter)

# Save to PDF
pdf_path = save_cover_letter_to_pdf(letter, filename="cover_letter1.pdf")
print(f"\n📝 PDF saved to: {pdf_path}")
